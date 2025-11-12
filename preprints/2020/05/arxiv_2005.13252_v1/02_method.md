---
authors:
- Fabien Le Floc'h
doc_id: arxiv:2005.13252v1
family_id: arxiv:2005.13252
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[2005.13252] Notes on the SWIFT method based on Shannon Wavelets for Option
  Pricing'
url_abs: http://arxiv.org/abs/2005.13252v1
url_html: https://ar5iv.org/html/2005.13252v1
venue: arXiv q-fin
version: 1
year: 2020
---


Fabien Le Floc’h

###### Abstract

This note shows that the cosine expansion based on the Vieta formula is equivalent to a discretization of the Parseval identity. We then evaluate the use of simple direct algorithms to compute the Shannon coefficients for the payoff. Finally, we explore the efficiency of a Filon quadrature instead of the Vieta formula for the coefficients related to the probability density function.

###### keywords:

SWIFT method, Wavelets, Heston, stochastic volatility, characteristic function, quantitative finance

## 1 Introduction

Ortiz-Gracia and
Oosterlee [[12](#bib.bib12)] describe a novel approach to the pricing of European options under models with a known characteristic function, based on Shannon Wavelets, referred to as the SWIFT method hereafter.
This note shows that the cosine expansion based on Vieta’s formula is equivalent to a discretization of Parseval’s identity. We then evaluate the use of simple direct algorithms to compute the Shannon coefficients for the payoff. Finally, we explore the efficiency of a Filon quadrature instead of Vieta’s formula for the coefficients related to the probability density function.

The equivalence with Parseval’s identity is also stated in [[11](#bib.bib11)].

## 2 Equivalence with Parseval’s identity

With the SWIFT method, the price at time t𝑡t of a Vanilla Put option of maturity T𝑇T and log-moneyness x=ln⁡FK𝑥𝐹𝐾x=\ln\frac{F}{K}, with K𝐾K the strike and forward F𝐹F is

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(x,t)=B​(t,T)​∑k=k1k2cm,k​Vm,k𝑣𝑥𝑡𝐵𝑡𝑇superscriptsubscript𝑘subscript𝑘1subscript𝑘2subscript𝑐  𝑚𝑘subscript𝑉  𝑚𝑘v(x,t)=B(t,T)\sum\_{k=k\_{1}}^{k\_{2}}c\_{m,k}V\_{m,k} |  | (1) |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | cm,ksubscript𝑐  𝑚𝑘\displaystyle c\_{m,k} | =⟨f|ϕm,k⟩=2m2​∫ℝf​(x)​ϕ​(2m​x−k)​𝑑x,,absentinner-product𝑓subscriptitalic-ϕ  𝑚𝑘superscript2𝑚2subscriptℝ𝑓𝑥italic-ϕsuperscript2𝑚𝑥𝑘differential-d𝑥\displaystyle=\left\langle f|\phi\_{m,k}\right\rangle=2^{\frac{m}{2}}\int\_{\mathbb{R}}f(x)\phi\left(2^{m}x-k\right)dx,, |  | (2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vm,ksubscript𝑉  𝑚𝑘\displaystyle V\_{m,k} | =∫Imv​(y,T)​ϕm,k​(y)​𝑑y,absentsubscriptsubscript𝐼𝑚𝑣𝑦𝑇subscriptitalic-ϕ  𝑚𝑘𝑦differential-d𝑦\displaystyle=\int\_{I\_{m}}v(y,T)\phi\_{m,k}(y)dy\,, |  | (3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ϕm,k​(x)subscriptitalic-ϕ  𝑚𝑘𝑥\displaystyle\phi\_{m,k}(x) | =2m2​ϕ​(2m​x−k),absentsuperscript2𝑚2italic-ϕsuperscript2𝑚𝑥𝑘\displaystyle=2^{\frac{m}{2}}\phi\left(2^{m}x-k\right)\,, |  | (4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ϕ​(x)italic-ϕ𝑥\displaystyle\phi(x) | =sin⁡π​xπ​xabsent𝜋𝑥𝜋𝑥\displaystyle=\frac{\sin\pi x}{\pi x} |  | (5) |

and k1,k2,m∈ℤ

subscript𝑘1subscript𝑘2𝑚
ℤk\_{1},k\_{2},m\in\mathbb{Z}, m>=1𝑚1m>=1 suitably chosen, f𝑓f the probability density function and v​(y,T)𝑣𝑦𝑇v(y,T) is the payoff at maturity with y=ln⁡F​(T,T)K𝑦𝐹𝑇𝑇𝐾y=\ln\frac{F(T,T)}{K}, that is v​(y,T)=K​|1−ey|+𝑣𝑦𝑇𝐾superscript1superscript𝑒𝑦v(y,T)=K|1-e^{y}|^{+} for a vanilla Put option.

In [[12](#bib.bib12)], the coefficients cm,ksubscript𝑐

𝑚𝑘c\_{m,k} and Vm,ksubscript𝑉

𝑚𝑘V\_{m,k} are computed using an approximation based on Vieta formula for the cardinal sinus:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(x)≈12J−1​∑j=12J−1cos⁡(2​j−12J​π​x)italic-ϕ𝑥1superscript2𝐽1superscriptsubscript𝑗1superscript2𝐽12𝑗1superscript2𝐽𝜋𝑥\phi(x)\approx\frac{1}{2^{J-1}}\sum\_{j=1}^{2^{J-1}}\cos\left(\frac{2j-1}{2^{J}}\pi x\right) |  | (6) |

where J𝐽J is chosen sufficiently large.

As mentioned in paragraph 3.1.2 of their paper, cm,ksubscript𝑐

𝑚𝑘c\_{m,k} can also be computed by Parseval’s identity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | cm,k=⟨f|ϕm,k⟩=12​π​⟨f^|ϕ^m,k⟩subscript𝑐  𝑚𝑘inner-product𝑓subscriptitalic-ϕ  𝑚𝑘12𝜋inner-product^𝑓subscript^italic-ϕ  𝑚𝑘c\_{m,k}=\left\langle f|\phi\_{m,k}\right\rangle=\frac{1}{2\pi}\left\langle\hat{f}|\hat{\phi}\_{m,k}\right\rangle |  | (7) |

where f^,ϕ^m,k

^𝑓subscript^italic-ϕ

𝑚𝑘\hat{f},\hat{\phi}\_{m,k} are the Fourier transforms of f𝑓f and ϕm,ksubscriptitalic-ϕ

𝑚𝑘\phi\_{m,k}. In particular f^​(z)=ψ​(−z)^𝑓𝑧𝜓𝑧\hat{f}(z)=\psi(-z) where ψ𝜓\psi is the characteristic function and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ^m,k​(w)=e−i​k2m​w2m2​rect(w2m+1​π)subscript^italic-ϕ  𝑚𝑘𝑤superscript𝑒𝑖𝑘superscript2𝑚𝑤superscript2𝑚2rect𝑤superscript2𝑚1𝜋\hat{\phi}\_{m,k}(w)=\frac{e^{-i\frac{k}{2^{m}}w}}{2^{\frac{m}{2}}}\operatorname\*{rect}\left(\frac{w}{2^{m+1}\pi}\right) |  | (8) |

where rectrect\operatorname\*{rect} is the rectangular function, that is rect(x)=1rect𝑥1\operatorname\*{rect}(x)=1 for |x|<12𝑥12|x|<\frac{1}{2}, rect(x)=12rect𝑥12\operatorname\*{rect}(x)=\frac{1}{2} for |x|=12𝑥12|x|=\frac{1}{2}, rect(x)=0rect𝑥0\operatorname\*{rect}(x)=0 for |x|>12𝑥12|x|>\frac{1}{2}.

Via a the change of variable t=w2m+1​π𝑡𝑤superscript2𝑚1𝜋t=\frac{w}{2^{m+1}\pi}, we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | cm,ksubscript𝑐  𝑚𝑘\displaystyle c\_{m,k} | =2m2​∫−1212[f^​(2m+1​π​t)​ei​2​π​k​t]​𝑑tabsentsuperscript2𝑚2superscriptsubscript1212delimited-[]^𝑓superscript2𝑚1𝜋𝑡superscript𝑒𝑖2𝜋𝑘𝑡differential-d𝑡\displaystyle=2^{\frac{m}{2}}\int\_{-\frac{1}{2}}^{\frac{1}{2}}\left[\hat{f}(2^{m+1}\pi t)e^{i2\pi kt}\right]dt |  | (9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =2m2+1​ℜ⁡[∫012f^​(2m+1​π​t)​ei​2​π​k​t​𝑑t]absentsuperscript2𝑚21superscriptsubscript012^𝑓superscript2𝑚1𝜋𝑡superscript𝑒𝑖2𝜋𝑘𝑡differential-d𝑡\displaystyle=2^{\frac{m}{2}+1}\Re\left[\int\_{0}^{\frac{1}{2}}\hat{f}(2^{m+1}\pi t)e^{i2\pi kt}dt\right] |  | (10) |

as ℜ⁡(ψ​(x))=ψ​(x)+ψ​(x)¯2=ψ​(x)+ψ​(−x)2𝜓𝑥𝜓𝑥¯𝜓𝑥2𝜓𝑥𝜓𝑥2\Re(\psi(x))=\frac{\psi(x)+\overline{\psi(x)}}{2}=\frac{\psi(x)+\psi(-x)}{2}.

Let us now discretize in 2J−1superscript2𝐽12^{J-1} equidistant steps equation ([10](#S2.E10 "In 2 Equivalence with Parseval’s identity ‣ Notes on the SWIFT method based on Shannon Wavelets for Option Pricing")) of size 12J1superscript2𝐽\frac{1}{2^{J}} at the mid-points tj=j−122Jsubscript𝑡𝑗𝑗12superscript2𝐽t\_{j}=\frac{j-\frac{1}{2}}{2^{J}} for j=1,2,…,2J−1𝑗

12…superscript2𝐽1j=1,2,...,2^{J-1}, we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | cm,k⋆superscriptsubscript𝑐  𝑚𝑘⋆\displaystyle c\_{m,k}^{\star} | =2m22J−1​∑j=12J−1ℜ⁡[f^​(2m​π​2​tj)​ei​π​k​2​tj]absentsuperscript2𝑚2superscript2𝐽1superscriptsubscript𝑗1superscript2𝐽1^𝑓superscript2𝑚𝜋2subscript𝑡𝑗superscript𝑒𝑖𝜋𝑘2subscript𝑡𝑗\displaystyle=\frac{2^{\frac{m}{2}}}{2^{J-1}}\sum\_{j=1}^{2^{J-1}}\Re\left[\hat{f}(2^{m}\pi 2t\_{j})e^{i\pi k2t\_{j}}\right] |  | (11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =2m22J−1​ℜ⁡[∑j=12J−1f^​(2m​π​(2​j−1)2J)​e2​i​π​k​j−122J]absentsuperscript2𝑚2superscript2𝐽1superscriptsubscript𝑗1superscript2𝐽1^𝑓superscript2𝑚𝜋2𝑗1superscript2𝐽superscript𝑒2𝑖𝜋𝑘𝑗12superscript2𝐽\displaystyle=\frac{2^{\frac{m}{2}}}{2^{J-1}}\Re\left[\sum\_{j=1}^{2^{J-1}}\hat{f}\left(\frac{2^{m}\pi(2j-1)}{2^{J}}\right)e^{2i\pi k\frac{j-\frac{1}{2}}{2^{J}}}\right] |  | (12) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =2m22J−1​ℜ⁡[ei​π​k2J​∑j=02J−1−1f^​(2m​π​(2​j−1)2J)​e2​i​π​k​j2J]absentsuperscript2𝑚2superscript2𝐽1superscript𝑒𝑖𝜋𝑘superscript2𝐽superscriptsubscript𝑗0superscript2𝐽11^𝑓superscript2𝑚𝜋2𝑗1superscript2𝐽superscript𝑒2𝑖𝜋𝑘𝑗superscript2𝐽\displaystyle=\frac{2^{\frac{m}{2}}}{2^{J-1}}\Re\left[e^{i\pi\frac{k}{2^{J}}}\sum\_{j=0}^{2^{J-1}-1}\hat{f}\left(\frac{2^{m}\pi(2j-1)}{2^{J}}\right)e^{2i\pi k\frac{j}{2^{J}}}\right] |  | (13) |

This is exactly equation (24) of [[12](#bib.bib12), p. B127] which corresponds to their expansion based on Vieta’s formula. Their expansion is thus equivalent to the mid-point quadrature applied to Parseval’s identity.

A particularly important property of equation [13](#S2.E13 "In 2 Equivalence with Parseval’s identity ‣ Notes on the SWIFT method based on Shannon Wavelets for Option Pricing") is that it can be computed by fast Fourier transform (FFT). The typical FFT algorithm computes the tranform (or inverse transform) from index 00 to n𝑛n. Here, we start with a negative index k1subscript𝑘1k\_{1}. The coefficients can be obtained with the relation

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝐜𝐜\displaystyle\mathbf{c} | =2m22J−1​ℜ⁡[𝐞T​ℱ−1​{𝐟}]absentsuperscript2𝑚2superscript2𝐽1superscript𝐞𝑇superscriptℱ1𝐟\displaystyle=\frac{2^{\frac{m}{2}}}{2^{J-1}}\Re\left[\mathbf{e}^{T}\mathcal{F}^{-1}\left\{\mathbf{f}\right\}\right] |  | (14) |

where ℱ−1superscriptℱ1\mathcal{F}^{-1} is the unscaled inverse discrete Fourier transform of size 2Jsuperscript2𝐽2^{J}, the vector 𝐟𝐟\mathbf{f} has elements fj=f^​(2m​π​(2​j+1)2J)​e2​i​π​k1​j2Jsubscript𝑓𝑗^𝑓superscript2𝑚𝜋2𝑗1superscript2𝐽superscript𝑒2𝑖𝜋subscript𝑘1𝑗superscript2𝐽f\_{j}=\hat{f}\left(\frac{2^{m}\pi(2j+1)}{2^{J}}\right)e^{2i\pi\frac{k\_{1}j}{2^{J}}} and the vector 𝐞𝐞\mathbf{e} has elements el=ei​π​l+k12Jsubscript𝑒𝑙superscript𝑒𝑖𝜋𝑙subscript𝑘1superscript2𝐽e\_{l}=e^{i\pi\frac{l+k\_{1}}{2^{J}}}. We also assumed that f^​(2m​π​(2​j+1)2J)=0^𝑓superscript2𝑚𝜋2𝑗1superscript2𝐽0\hat{f}\left(\frac{2^{m}\pi(2j+1)}{2^{J}}\right)=0 for j≥2J−1𝑗superscript2𝐽1j\geq 2^{J-1}.
This leads to a very efficient way to compute the coefficients cm,ksubscript𝑐

𝑚𝑘c\_{m,k}, for all k𝑘k, together. In practice, this means that the bounds k1≤k<k2subscript𝑘1𝑘subscript𝑘2k\_{1}\leq k<k\_{2} are chosen so that k2−k1<2Jsubscript𝑘2subscript𝑘1superscript2𝐽k\_{2}-k\_{1}<2^{J}.

In particular, if we center the interval around zero, that is for k1=−2J−1subscript𝑘1superscript2𝐽1k\_{1}=-2^{J-1}, we can save a bit of computation by directly using fj=f^​(2m​π​(2​j+1)2J)subscript𝑓𝑗^𝑓superscript2𝑚𝜋2𝑗1superscript2𝐽f\_{j}=\hat{f}\left(\frac{2^{m}\pi(2j+1)}{2^{J}}\right) and swapping (g0,…,g2J−1)subscript𝑔0…subscript𝑔superscript2𝐽1(g\_{0},...,g\_{2^{J-1}}) with (g2J−1,…​g2J−1)subscript𝑔superscript2𝐽1…subscript𝑔superscript2𝐽1(g\_{2^{J}-1},...g\_{2^{J}-1}) where 𝐠=ℱ−1​{𝐟}𝐠superscriptℱ1𝐟\mathbf{g}=\mathcal{F}^{-1}\left\{\mathbf{f}\right\}.

## 3 Alternative quadratures

### 3.1 Trapezoidal

Instead of the mid-point method, we could have considered the trapezoidal method, this would result in

|  |  |  |  |
| --- | --- | --- | --- |
|  | cm,k⋆=2m22J−1​ℜ⁡[∑j=02J−1−1wj​f^​(2m​π​(2​j)2J)​e2​i​π​k​j2J]superscriptsubscript𝑐  𝑚𝑘⋆superscript2𝑚2superscript2𝐽1superscriptsubscript𝑗0superscript2𝐽11subscript𝑤𝑗^𝑓superscript2𝑚𝜋2𝑗superscript2𝐽superscript𝑒2𝑖𝜋𝑘𝑗superscript2𝐽c\_{m,k}^{\star}=\frac{2^{\frac{m}{2}}}{2^{J-1}}\Re\left[\sum\_{j=0}^{2^{J-1}-1}w\_{j}\hat{f}\left(\frac{2^{m}\pi(2j)}{2^{J}}\right)e^{2i\pi k\frac{j}{2^{J}}}\right] |  | (15) |

where wj=1subscript𝑤𝑗1w\_{j}=1 for j≥1𝑗1j\geq 1 and w0=12subscript𝑤012w\_{0}=\frac{1}{2}.

The fast inverse discrete Fourier transform of length 2Jsuperscript2𝐽2^{J} can be directly used to compute cm,ksubscript𝑐

𝑚𝑘c\_{m,k} by using fj=f^​(2m​π​(2​j)2J)subscript𝑓𝑗^𝑓superscript2𝑚𝜋2𝑗superscript2𝐽f\_{j}=\hat{f}\left(\frac{2^{m}\pi(2j)}{2^{J}}\right) for 1≤j<2J−11𝑗superscript2𝐽11\leq j<2^{J-1}, fj=0subscript𝑓𝑗0f\_{j}=0 for 2J−1≤jsuperscript2𝐽1𝑗2^{J-1}\leq j, and f0=12​f^​(0)subscript𝑓012^𝑓0f\_{0}=\frac{1}{2}\hat{f}(0).

We will see in the numerical examples that it can be much more accurate than the mid-point method.

In the same framework, we could also explore other quadratures, such as the Simpson’s quadrature. The problem is that those tend to behave worse than the midpoint or trapezoidal rules on oscillatory functions. In fact, the trapezoidal rule can achieve exponential convergence on oscillatory functions [[5](#bib.bib5), [14](#bib.bib14)]. In the case of the probability density transform function f^^𝑓\hat{f}, this can be also be seen from the Euler-Maclaurin formula where as all the derivatives f^(2​l+1)​(2m​π)superscript^𝑓2𝑙1superscript2𝑚𝜋\hat{f}^{(2l+1)}\left(2^{m}\pi\right) will be small if the characteristic function decreases exponentially.

### 3.2 Adaptive Filon

Instead of quadrature with a fixed number of steps, we can use an adaptive Filon quadrature to compute the coefficients cm,ksubscript𝑐

𝑚𝑘c\_{m,k} by equation ([10](#S2.E10 "In 2 Equivalence with Parseval’s identity ‣ Notes on the SWIFT method based on Shannon Wavelets for Option Pricing")). This is particularly interesting since the cost of computing the characteristic function is relatively high.

Is it more important to reduce its number of evaluations than to use Fast Fourier Transform tricks to compute cm,ksubscript𝑐

𝑚𝑘c\_{m,k}?
We will explore this in the numerical examples (section [8](#S8 "8 Numerical examples ‣ Notes on the SWIFT method based on Shannon Wavelets for Option Pricing")).

An alternative adaptive quadrature, close in spirit, is to use an adaptive cubic-Hermite quadrature to integrate f^^𝑓\hat{f}, and use the integration nodes to compute the piecewise cubic Hermite interpolant of f^^𝑓\hat{f}. Then we can use the trapezoidal-FFT approach on a dense discretization. This saves explicit computations of the characteristic function while still allowing the use of the FFT algorithm.

## 4 Sine and Exponential integrals for the payoff

For a Vanilla Put option, the payoff at maturity is V​(y,T)=K​(1−ey)+𝑉𝑦𝑇𝐾superscript1superscript𝑒𝑦V(y,T)=K(1-e^{y})^{+}. According to equation ([3](#S2.E3 "In 2 Equivalence with Parseval’s identity ‣ Notes on the SWIFT method based on Shannon Wavelets for Option Pricing")), the payoffs coefficients are then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vm,ksubscript𝑉  𝑚𝑘\displaystyle V\_{m,k} | =K​2m2​∫a0(1−ey)​sin⁡(π​(2m​y−k))π​(2m​y−k)​𝑑yabsent𝐾superscript2𝑚2superscriptsubscript𝑎01superscript𝑒𝑦𝜋superscript2𝑚𝑦𝑘𝜋superscript2𝑚𝑦𝑘differential-d𝑦\displaystyle=K2^{\frac{m}{2}}\int\_{a}^{0}(1-e^{y})\frac{\sin\left(\pi\left(2^{m}y-k\right)\right)}{\pi\left(2^{m}y-k\right)}dy |  | (16) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =K​2m2​∫a0sin⁡(π​(2m​y−k))π​(2m​y−k)​𝑑y−K​2m2​∫a0ey​sin⁡(π​(2m​y−k))π​(2m​y−k)​𝑑yabsent𝐾superscript2𝑚2superscriptsubscript𝑎0𝜋superscript2𝑚𝑦𝑘𝜋superscript2𝑚𝑦𝑘differential-d𝑦𝐾superscript2𝑚2superscriptsubscript𝑎0superscript𝑒𝑦𝜋superscript2𝑚𝑦𝑘𝜋superscript2𝑚𝑦𝑘differential-d𝑦\displaystyle=K2^{\frac{m}{2}}\int\_{a}^{0}\frac{\sin\left(\pi\left(2^{m}y-k\right)\right)}{\pi\left(2^{m}y-k\right)}dy-K2^{\frac{m}{2}}\int\_{a}^{0}e^{y}\frac{\sin\left(\pi\left(2^{m}y-k\right)\right)}{\pi\left(2^{m}y-k\right)}dy |  | (17) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =K2m2​π​∫π​(2m​a−k)−π​ksin⁡tt​𝑑t−K​ek2m2m2​π​∫π​(2m​a−k)−π​ketπ​2m​sin⁡tt​𝑑tabsent𝐾superscript2𝑚2𝜋superscriptsubscript𝜋superscript2𝑚𝑎𝑘𝜋𝑘𝑡𝑡differential-d𝑡𝐾superscript𝑒𝑘superscript2𝑚superscript2𝑚2𝜋superscriptsubscript𝜋superscript2𝑚𝑎𝑘𝜋𝑘superscript𝑒𝑡𝜋superscript2𝑚𝑡𝑡differential-d𝑡\displaystyle=\frac{K}{2^{\frac{m}{2}}\pi}\int\_{\pi\left(2^{m}a-k\right)}^{-\pi k}\frac{\sin t}{t}dt-\frac{Ke^{\frac{k}{2^{m}}}}{2^{\frac{m}{2}}\pi}\int\_{\pi\left(2^{m}a-k\right)}^{-\pi k}e^{\frac{t}{\pi 2^{m}}}\frac{\sin t}{t}dt |  | (18) |

The first integral corresponds the sine integral Si​(x)=∫0xsin⁡tt​𝑑tSi𝑥superscriptsubscript0𝑥𝑡𝑡differential-d𝑡\textsf{Si}(x)=\int\_{0}^{x}\frac{\sin t}{t}dt. Many efficient algorithms exist to compute it [[9](#bib.bib9), [4](#bib.bib4)]. Most mathematical software (for example Octave, Matlab) or libraries (for example netlib) include the function. It can effectively be considered as a closed form function.

The second integral can be reduced to evaluations of the complementary exponential integral Ein​(z)=∫0z1−e−tt​𝑑tEin𝑧superscriptsubscript0𝑧1superscript𝑒𝑡𝑡differential-d𝑡\textsf{Ein}(z)=\int\_{0}^{z}\frac{1-e^{-t}}{t}dt in the complex plane. In deed, it can be verified that we have the identity

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01e−a​t​sin⁡(b​t)t​𝑑t=ℑ⁡Ein​(a+i​b)superscriptsubscript01superscript𝑒𝑎𝑡𝑏𝑡𝑡differential-d𝑡Ein𝑎𝑖𝑏\int\_{0}^{1}\frac{e^{-at}\sin(bt)}{t}dt=\Im\textsf{Ein}(a+ib) |  | (19) |

The complementary exponential integral is related to the exponential integral Ei​(z)=−∫z∞e−tt​𝑑tEi𝑧superscriptsubscript𝑧superscript𝑒𝑡𝑡differential-d𝑡\textsf{Ei}(z)=-\int\_{z}^{\infty}\frac{e^{-t}}{t}dt by the relation Ein​(z)=γ+ln⁡|z|+i​ℑ⁡(−z)​|arg⁡(−z)|−Ei​(−z)Ein𝑧𝛾𝑧𝑖𝑧𝑧Ei𝑧\textsf{Ein}(z)=\gamma+\ln|z|+i\Im(-z)|\arg(-z)|-\textsf{Ei}(-z). Again many efficient algorithms exist to compute the complementary exponential integral [[1](#bib.bib1), [4](#bib.bib4), [13](#bib.bib13)].

In terms of those special functions, the coefficients are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vm,k=K2m2​π​ek2m​ℑ⁡[Ein​(−taπ​2m+i​ta)−Ein​(−t0π​2m+i​t0)]−K2m2​π​[Si​(ta)−Si​(t0)]subscript𝑉  𝑚𝑘𝐾superscript2𝑚2𝜋superscript𝑒𝑘superscript2𝑚Einsubscript𝑡𝑎𝜋superscript2𝑚𝑖subscript𝑡𝑎Einsubscript𝑡0𝜋superscript2𝑚𝑖subscript𝑡0𝐾superscript2𝑚2𝜋delimited-[]Sisubscript𝑡𝑎Sisubscript𝑡0V\_{m,k}=\frac{K}{2^{\frac{m}{2}}\pi}e^{\frac{k}{2^{m}}}\Im\left[\textsf{Ein}\left(-\frac{t\_{a}}{\pi 2^{m}}+it\_{a}\right)-\textsf{Ein}\left(-\frac{t\_{0}}{\pi 2^{m}}+it\_{0}\right)\right]-\frac{K}{2^{\frac{m}{2}}\pi}\left[\textsf{Si}(t\_{a})-\textsf{Si}(t\_{0})\right] |  | (20) |

with ta=π​(2m​a−k)subscript𝑡𝑎𝜋superscript2𝑚𝑎𝑘t\_{a}=\pi\left(2^{m}a-k\right) and t0=−π​ksubscript𝑡0𝜋𝑘t\_{0}=-\pi k.

The expansion based on Vieta’s formula might require thousands of terms to reach an acceptable accuracy (Table [1](#S4.T1 "Table 1 ‣ 4 Sine and Exponential integrals for the payoff ‣ Notes on the SWIFT method based on Shannon Wavelets for Option Pricing")). With the same number of terms, a Simpson 3/8 quadrature is more accurate and faster to compute. Our simple implementation of the algorithm from Pegoraro and
Slusallek [[13](#bib.bib13)] is much faster and achieves machine epsilon accuracy while the algorithm from the CERN libary Mathlib [[6](#bib.bib6)] is even faster for a close to machine epsilon accuracy as it relies on simple rational and padé expansions in the zone of interest. In practice, the implementation of the SWIFT method will still benefit from a cache table of Vm,ksubscript𝑉

𝑚𝑘V\_{m,k} for example for m∈{2,…,8}𝑚2…8m\in\{2,...,8\} and k∈{−512,…,512}𝑘512…512k\in\{-512,...,512\}.

Table 1: Vm,ksubscript𝑉

𝑚𝑘V\_{m,k} for m=6𝑚6m=6, k=−1𝑘1k=-1, a=−1𝑎1a=-1. Vieta’s formula or Simpson’s quadrature use 2J−1superscript2𝐽12^{J-1} terms.

| Method | Value | Time(ns) |
| --- | --- | --- |
| Vieta J=5𝐽5J=5 | -0.0555195115435162 | 600 |
| Simpson J=5𝐽5J=5 | -0.0020905045216672 | 520 |
| Vieta J=10𝐽10J=10 | 0.0020428901436639 | 17300 |
| Simpson J=10𝐽10J=10 | 0.0020420973936057 | 15300 |
| CERN | 0.0020420954069492 | 420 |
| Pegoraro | 0.0020420954069488 | 2500 |

## 5 Alternative payoff coefficients

The interval [a,b]𝑎𝑏[a,b] is centered along the spot F​(0,T)𝐹0𝑇F(0,T), we can express the payoff in terms of the spot F​(0,T)𝐹0𝑇F(0,T) instead of the strike K𝐾K. This leads to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vm,ksubscript𝑉  𝑚𝑘\displaystyle V\_{m,k} | =2m2​∫abF​|KF−ey|+​sin⁡(π​(2m​y−k))π​(2m​y−k)​𝑑yabsentsuperscript2𝑚2superscriptsubscript𝑎𝑏𝐹superscript𝐾𝐹superscript𝑒𝑦𝜋superscript2𝑚𝑦𝑘𝜋superscript2𝑚𝑦𝑘differential-d𝑦\displaystyle=2^{\frac{m}{2}}\int\_{a}^{b}F\left|\frac{K}{F}-e^{y}\right|^{+}\frac{\sin\left(\pi\left(2^{m}y-k\right)\right)}{\pi\left(2^{m}y-k\right)}dy |  | (21) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =F​2m2​∫az(ez−ey)​sin⁡(π​(2m​y−k))π​(2m​y−k)​𝑑yabsent𝐹superscript2𝑚2superscriptsubscript𝑎𝑧superscript𝑒𝑧superscript𝑒𝑦𝜋superscript2𝑚𝑦𝑘𝜋superscript2𝑚𝑦𝑘differential-d𝑦\displaystyle=F2^{\frac{m}{2}}\int\_{a}^{z}\left(e^{z}-e^{y}\right)\frac{\sin\left(\pi\left(2^{m}y-k\right)\right)}{\pi\left(2^{m}y-k\right)}dy |  | (22) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =K​e−z​2m2​∫az(ez−ey)​sin⁡(π​(2m​y−k))π​(2m​y−k)​𝑑yabsent𝐾superscript𝑒𝑧superscript2𝑚2superscriptsubscript𝑎𝑧superscript𝑒𝑧superscript𝑒𝑦𝜋superscript2𝑚𝑦𝑘𝜋superscript2𝑚𝑦𝑘differential-d𝑦\displaystyle=Ke^{-z}2^{\frac{m}{2}}\int\_{a}^{z}\left(e^{z}-e^{y}\right)\frac{\sin\left(\pi\left(2^{m}y-k\right)\right)}{\pi\left(2^{m}y-k\right)}dy |  | (23) |

where z=ln⁡KF𝑧𝐾𝐹z=\ln\frac{K}{F} and y=ln⁡STF𝑦subscript𝑆𝑇𝐹y=\ln\frac{S\_{T}}{F}.

In terms of those special functions, the coefficients are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vm,k​(z)=K​ek2m−z2m2​π​ℑ⁡[Ein​(−taπ​2m+i​ta)−Ein​(−tzπ​2m+i​tz)]−K2m2​π​[Si​(ta)−Si​(tz)]subscript𝑉  𝑚𝑘𝑧𝐾superscript𝑒𝑘superscript2𝑚𝑧superscript2𝑚2𝜋Einsubscript𝑡𝑎𝜋superscript2𝑚𝑖subscript𝑡𝑎Einsubscript𝑡𝑧𝜋superscript2𝑚𝑖subscript𝑡𝑧𝐾superscript2𝑚2𝜋delimited-[]Sisubscript𝑡𝑎Sisubscript𝑡𝑧V\_{m,k}(z)=\frac{Ke^{\frac{k}{2^{m}}-z}}{2^{\frac{m}{2}}\pi}\Im\left[\textsf{Ein}\left(-\frac{t\_{a}}{\pi 2^{m}}+it\_{a}\right)-\textsf{Ein}\left(-\frac{t\_{z}}{\pi 2^{m}}+it\_{z}\right)\right]-\frac{K}{2^{\frac{m}{2}}\pi}\left[\textsf{Si}(t\_{a})-\textsf{Si}(t\_{z})\right] |  | (24) |

with ta=π​(2m​a−k)subscript𝑡𝑎𝜋superscript2𝑚𝑎𝑘t\_{a}=\pi\left(2^{m}a-k\right) and tz=π​(2m​z−k)subscript𝑡𝑧𝜋superscript2𝑚𝑧𝑘t\_{z}=\pi\left(2^{m}z-k\right).

The price of the option of strike K𝐾K corresponds then to v​(0,t)𝑣0𝑡v(0,t). The coefficients cm,ksubscript𝑐

𝑚𝑘c\_{m,k} become independent of x𝑥x. This is nearly equivalent to the Levy based equation (33) in [[12](#bib.bib12)] that defines the coefficients Vm,kα​(x)superscriptsubscript𝑉

𝑚𝑘𝛼𝑥V\_{m,k}^{\alpha}(x). The difference lies in the interval considered. In their paper, Vm,kα​(x)=∫abK​|1−eu|+​ϕm,k​(u+z)​𝑑usuperscriptsubscript𝑉

𝑚𝑘𝛼𝑥superscriptsubscript𝑎𝑏𝐾superscript1superscript𝑒𝑢subscriptitalic-ϕ

𝑚𝑘𝑢𝑧differential-d𝑢V\_{m,k}^{\alpha}(x)=\int\_{a}^{b}K|1-e^{u}|^{+}\phi\_{m,k}(u+z)du with u=ln⁡STK𝑢subscript𝑆𝑇𝐾u=\ln\frac{S\_{T}}{K}. This can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vm,kα​(x)=K​∫a+zz(1−et−z)​ϕm,k​(t)​𝑑tsuperscriptsubscript𝑉  𝑚𝑘𝛼𝑥𝐾superscriptsubscript𝑎𝑧𝑧1superscript𝑒𝑡𝑧subscriptitalic-ϕ  𝑚𝑘𝑡differential-d𝑡V\_{m,k}^{\alpha}(x)=K\int\_{a+z}^{z}\left(1-e^{t-z}\right)\phi\_{m,k}(t)dt |  | (25) |

with the change of variable t=u+z𝑡𝑢𝑧t=u+z. The interval [a,b]𝑎𝑏[a,b] is thus shifted from z𝑧z upwards. Our choice of interval is more accurate as it corresponds directly to the Levy characteristic function, while their interval is based on the shifted Levy characteristic function. Also their Levy formulation (as well as ours) leads to options prices different from the classic formulation: for the two to be equivalent, the integers k1subscript𝑘1k\_{1} and k2subscript𝑘2k\_{2} should be adjusted to k1=2m​(a+z)subscript𝑘1superscript2𝑚𝑎𝑧k\_{1}=2^{m}(a+z) and k2=2m​(b+z)subscript𝑘2superscript2𝑚𝑏𝑧k\_{2}=2^{m}(b+z). But then some of the density coefficients need to be recomputed at each strike as the window [k1,k2]subscript𝑘1subscript𝑘2[k\_{1},k\_{2}] moves forward as z𝑧z increases and the Levy approach loses in efficiency.

Another advantage of having cm,ksubscript𝑐

𝑚𝑘c\_{m,k} independent of the strike is that the integers k1subscript𝑘1k\_{1} and k2subscript𝑘2k\_{2} can also be determined in a strike independent manner from the value of the density coefficients cm,ksubscript𝑐

𝑚𝑘c\_{m,k} and the area under the curve defined by the probability density (which should sum to one minus a user-defined tolerance) as explained by Ortiz-Gracia and
Oosterlee [[12](#bib.bib12)], instead of relying on the relatively rough guess given by the cumulants (the fixed interval [a,b]𝑎𝑏[a,b]). With the cumulants approach, it is not always obvious how large the truncation level L𝐿L should be chosen to achieve a desired accuracy.

## 6 Alternative FFT-compatible payoff coefficients

In a similar fashion to Maree
et al. [[11](#bib.bib11)], we start from the definition

|  |  |  |  |
| --- | --- | --- | --- |
|  | sin⁡(π​x)π​x=∫01cos⁡(π​x​w)​𝑑w.𝜋𝑥𝜋𝑥superscriptsubscript01𝜋𝑥𝑤differential-d𝑤\frac{\sin(\pi x)}{\pi x}=\int\_{0}^{1}\cos(\pi xw)dw\,. |  | (26) |

We can then choose an appropriate discretization that has good convergence, and is allows computation of the payoff coefficients Vm,ksubscript𝑉

𝑚𝑘V\_{m,k} by the FFT. The choice from Ortiz-Gracia and
Oosterlee [[12](#bib.bib12)] is equivalent to the mid-point quadrature. On this problem, the Trapezoidal rule would not lead to an increase in accuracy111It can be shown that the mid-point is actually more accurate by a factor of two.. A particularly simple an effective choice is the second Euler-Maclaurin summation formula, that is the Euler-Maclaurin extension to the mid-point rule.

|  |  |  |  |
| --- | --- | --- | --- |
|  | sin⁡(π​x)π​x≈1N​∑n=0N−1cos⁡(π​x​2​n+12​N)+π​x24​N2​sin⁡(π​x).𝜋𝑥𝜋𝑥1𝑁superscriptsubscript𝑛0𝑁1𝜋𝑥2𝑛12𝑁𝜋𝑥24superscript𝑁2𝜋𝑥\frac{\sin(\pi x)}{\pi x}\approx\frac{1}{N}\sum\_{n=0}^{N-1}\cos\left(\pi x\frac{2n+1}{2N}\right)+\frac{\pi x}{24N^{2}}\sin(\pi x)\,. |  | (27) |

Using the above in equation ([23](#S5.E23 "In 5 Alternative payoff coefficients ‣ Notes on the SWIFT method based on Shannon Wavelets for Option Pricing")) leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vm,ksubscript𝑉  𝑚𝑘\displaystyle V\_{m,k} | =K​e−z​2m2N​∑n=1N−1∫az(ez−ey)​cos⁡(π​(2m​y−k)​2​n+12​N)​𝑑yabsent𝐾superscript𝑒𝑧superscript2𝑚2𝑁superscriptsubscript𝑛1𝑁1superscriptsubscript𝑎𝑧superscript𝑒𝑧superscript𝑒𝑦𝜋superscript2𝑚𝑦𝑘2𝑛12𝑁differential-d𝑦\displaystyle=\frac{Ke^{-z}2^{\frac{m}{2}}}{N}\sum\_{n=1}^{N-1}\int\_{a}^{z}\left(e^{z}-e^{y}\right)\cos\left(\pi\left(2^{m}y-k\right)\frac{2n+1}{2N}\right)dy |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +π24​N2​K​e−z​2m2​∫az(2m​y−k)​(ez−ey)​sin⁡(π​(2m​y−k))​𝑑y𝜋24superscript𝑁2𝐾superscript𝑒𝑧superscript2𝑚2superscriptsubscript𝑎𝑧superscript2𝑚𝑦𝑘superscript𝑒𝑧superscript𝑒𝑦𝜋superscript2𝑚𝑦𝑘differential-d𝑦\displaystyle+\frac{\pi}{24N^{2}}Ke^{-z}2^{\frac{m}{2}}\int\_{a}^{z}\left(2^{m}y-k\right)\left(e^{z}-e^{y}\right)\sin\left(\pi\left(2^{m}y-k\right)\right)dy |  | (28) |

Let Cn​(a,z)=∫az(ez−ey)​cos⁡(π​2m​y​nN)​𝑑ysubscript𝐶𝑛𝑎𝑧superscriptsubscript𝑎𝑧superscript𝑒𝑧superscript𝑒𝑦𝜋superscript2𝑚𝑦𝑛𝑁differential-d𝑦C\_{n}(a,z)=\int\_{a}^{z}\left(e^{z}-e^{y}\right)\cos\left(\pi 2^{m}y\frac{n}{N}\right)dy and Sn​(a,z)=∫az(ez−ey)​sin⁡(π​2m​y​nN)​𝑑ysubscript𝑆𝑛𝑎𝑧superscriptsubscript𝑎𝑧superscript𝑒𝑧superscript𝑒𝑦𝜋superscript2𝑚𝑦𝑛𝑁differential-d𝑦S\_{n}(a,z)=\int\_{a}^{z}\left(e^{z}-e^{y}\right)\sin\left(\pi 2^{m}y\frac{n}{N}\right)dy. Using the trigonometric cos and sin identities, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vm,ksubscript𝑉  𝑚𝑘\displaystyle V\_{m,k} | =K​e−z​2m2N​∑n=0N−1Cn+12​(a,z)​cos⁡(π​k​2​n+12​N)+Sn+12​(a,z)​sin⁡(π​k​2​n+12​N)absent𝐾superscript𝑒𝑧superscript2𝑚2𝑁superscriptsubscript𝑛0𝑁1subscript𝐶𝑛12𝑎𝑧𝜋𝑘2𝑛12𝑁subscript𝑆𝑛12𝑎𝑧𝜋𝑘2𝑛12𝑁\displaystyle=\frac{Ke^{-z}2^{\frac{m}{2}}}{N}\sum\_{n=0}^{N-1}C\_{n+\frac{1}{2}}(a,z)\cos\left(\pi k\frac{2n+1}{2N}\right)+S\_{n+\frac{1}{2}}(a,z)\sin\left(\pi k\frac{2n+1}{2N}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −(−1)k​π​k24​N2​K​e−z​2m2​SN​(a,z)−(−1)k24​N2​K​e−z​2m2​D​(a,z)superscript1𝑘𝜋𝑘24superscript𝑁2𝐾superscript𝑒𝑧superscript2𝑚2subscript𝑆𝑁𝑎𝑧superscript1𝑘24superscript𝑁2𝐾superscript𝑒𝑧superscript2𝑚2𝐷𝑎𝑧\displaystyle-\frac{(-1)^{k}\pi k}{24N^{2}}Ke^{-z}2^{\frac{m}{2}}S\_{N}(a,z)\ -\frac{(-1)^{k}}{24N^{2}}Ke^{-z}2^{\frac{m}{2}}D(a,z) |  | (29) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​(a,z)𝐷𝑎𝑧\displaystyle D(a,z) | =ez​((pm4+pm2)​z−3​pm2−1)​sin⁡(pm​z)+((pm3+pm)​z+2​pm3)​cos⁡(pm​z)pm​(pm4+2​pm2+1)absentsuperscript𝑒𝑧superscriptsubscript𝑝𝑚4superscriptsubscript𝑝𝑚2𝑧3superscriptsubscript𝑝𝑚21subscript𝑝𝑚𝑧superscriptsubscript𝑝𝑚3subscript𝑝𝑚𝑧2superscriptsubscript𝑝𝑚3subscript𝑝𝑚𝑧subscript𝑝𝑚superscriptsubscript𝑝𝑚42superscriptsubscript𝑝𝑚21\displaystyle=e^{z}\frac{\left(\left({{{{p}\_{m}}}^{4}}+{{{{p}\_{m}}}^{2}}\right)z-3{{{{p}\_{m}}}^{2}}-1\right)\,\sin{\left({{p}\_{m}}z\right)}+\left(\left({{{{p}\_{m}}}^{3}}+{{p}\_{m}}\right)z+2{{{{p}\_{m}}}^{3}}\right)\,\cos{\left({{p}\_{m}}z\right)}}{{p}\_{m}(p\_{m}^{4}+2{{{{p}\_{m}}}^{2}}+1)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ez​(pm4+2​pm2+1)​sin⁡(a​pm)+(−a​pm5−2​a​pm3−a​pm)​cos⁡(a​pm)pm​(pm4+2​pm2+1)superscript𝑒𝑧superscriptsubscript𝑝𝑚42superscriptsubscript𝑝𝑚21𝑎subscript𝑝𝑚𝑎superscriptsubscript𝑝𝑚52𝑎superscriptsubscript𝑝𝑚3𝑎subscript𝑝𝑚𝑎subscript𝑝𝑚subscript𝑝𝑚superscriptsubscript𝑝𝑚42superscriptsubscript𝑝𝑚21\displaystyle+e^{z}\frac{\left({{{{p}\_{m}}}^{4}}+2{{{{p}\_{m}}}^{2}}+1\right)\sin{\left(a\,{{p}\_{m}}\right)}+\left(-a\,{{{{p}\_{m}}}^{5}}-2a\,{{{{p}\_{m}}}^{3}}-a\,{{p}\_{m}}\right)\cos{\left(a\,{{p}\_{m}}\right)}}{{p}\_{m}(p\_{m}^{4}+2{{{{p}\_{m}}}^{2}}+1)} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +ea​((−a−1)​pm4+(1−a)​pm2)​sin⁡(a​pm)+(a​pm5+(a−2)​pm3)​cos⁡(a​pm)pm​(pm4+2​pm2+1),superscript𝑒𝑎𝑎1superscriptsubscript𝑝𝑚41𝑎superscriptsubscript𝑝𝑚2𝑎subscript𝑝𝑚𝑎superscriptsubscript𝑝𝑚5𝑎2superscriptsubscript𝑝𝑚3𝑎subscript𝑝𝑚subscript𝑝𝑚superscriptsubscript𝑝𝑚42superscriptsubscript𝑝𝑚21\displaystyle+e^{a}\frac{\left(\left(-a-1\right)\,{{{{p}\_{m}}}^{4}}+\left(1-a\right)\,{{{{p}\_{m}}}^{2}}\right)\sin{\left(a\,{{p}\_{m}}\right)}+\left(a\,{{{{p}\_{m}}}^{5}}+\left(a-2\right)\,{{{{p}\_{m}}}^{3}}\right)\cos{\left(a\,{{p}\_{m}}\right)}}{{p}\_{m}(p\_{m}^{4}+2{{{{p}\_{m}}}^{2}}+1)}\,, |  | (30) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Cn​(a,z)subscript𝐶𝑛𝑎𝑧\displaystyle C\_{n}(a,z) | =ez​sin⁡(qn,m​z)−qn,m​cos⁡(qn,m​z)qn,m​(1+qn,m2)−ez​sin⁡(qn,m​a)qn,mabsentsuperscript𝑒𝑧subscript𝑞  𝑛𝑚𝑧subscript𝑞  𝑛𝑚subscript𝑞  𝑛𝑚𝑧subscript𝑞  𝑛𝑚1superscriptsubscript𝑞  𝑛𝑚2superscript𝑒𝑧subscript𝑞  𝑛𝑚𝑎subscript𝑞  𝑛𝑚\displaystyle=e^{z}\frac{\sin\left(q\_{n,m}z\right)-q\_{n,m}\cos\left(q\_{n,m}z\right)}{q\_{n,m}(1+q\_{n,m}^{2})}-e^{z}\frac{\sin\left(q\_{n,m}a\right)}{q\_{n,m}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +ea​cos⁡(qn,m​a)+qn,m​sin⁡(qn,m​a)1+qn,m2,superscript𝑒𝑎subscript𝑞  𝑛𝑚𝑎subscript𝑞  𝑛𝑚subscript𝑞  𝑛𝑚𝑎1superscriptsubscript𝑞  𝑛𝑚2\displaystyle+e^{a}\frac{\cos\left(q\_{n,m}a\right)+q\_{n,m}\sin\left(q\_{n,m}a\right)}{1+q\_{n,m}^{2}}\,, |  | (31) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Sn​(a,z)subscript𝑆𝑛𝑎𝑧\displaystyle S\_{n}(a,z) | =−ez​cos⁡(qn,m​z)+qn,m​sin⁡(qn,m​z)qn,m​(1+qn,m2)+ez​cos⁡(qn,m​a)qn,mabsentsuperscript𝑒𝑧subscript𝑞  𝑛𝑚𝑧subscript𝑞  𝑛𝑚subscript𝑞  𝑛𝑚𝑧subscript𝑞  𝑛𝑚1superscriptsubscript𝑞  𝑛𝑚2superscript𝑒𝑧subscript𝑞  𝑛𝑚𝑎subscript𝑞  𝑛𝑚\displaystyle=-e^{z}\frac{\cos\left(q\_{n,m}z\right)+q\_{n,m}\sin\left(q\_{n,m}z\right)}{q\_{n,m}(1+q\_{n,m}^{2})}+e^{z}\frac{\cos\left(q\_{n,m}a\right)}{q\_{n,m}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +ea​sin⁡(qn,m​a)−qn,m​cos⁡(qn,m​a)1+qn,m2,superscript𝑒𝑎subscript𝑞  𝑛𝑚𝑎subscript𝑞  𝑛𝑚subscript𝑞  𝑛𝑚𝑎1superscriptsubscript𝑞  𝑛𝑚2\displaystyle+e^{a}\frac{\sin\left(q\_{n,m}a\right)-q\_{n,m}\cos\left(q\_{n,m}a\right)}{1+q\_{n,m}^{2}}\,, |  | (32) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | qn,msubscript𝑞  𝑛𝑚\displaystyle q\_{n,m} | =nN​pm,absent𝑛𝑁subscript𝑝𝑚\displaystyle=\frac{n}{N}p\_{m}\,, |  | (33) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | pmsubscript𝑝𝑚\displaystyle p\_{m} | =π​2m.absent𝜋superscript2𝑚\displaystyle=\pi 2^{m}\,. |  | (34) |

In particular, SNsubscript𝑆𝑁S\_{N} and D𝐷D are independent of k𝑘k. Computing Vm,ksubscript𝑉

𝑚𝑘V\_{m,k} with the Euler-Maclauring correction for all k𝑘k requires only k𝑘k more multiplications than the mid-point quadrature. The sum over n𝑛n corresponds to the mid-point quadrature, and can be computed with two fast Fourier transforms of size N𝑁N (see appendix A).

## 7 Choice of m𝑚m and k1,k2 subscript𝑘1subscript𝑘2k\_{1},k\_{2}

The SWIFT method accuracy is fully determined by the choice of the scale m𝑚m and the truncation k1,k2

subscript𝑘1subscript𝑘2k\_{1},k\_{2}. There is some interplay between those since the scale m𝑚m also determines the truncation of the characteristic function: the characteristic function will not be evaluated beyond 2m​πsuperscript2𝑚𝜋2^{m}\pi.

If we want to use the radix-2 FFT algorithm to compute the payoff coefficients Vm,ksubscript𝑉

𝑚𝑘V\_{m,k}, there is little reason not to use k2−k1=2Jsubscript𝑘2subscript𝑘1superscript2𝐽k\_{2}-k\_{1}=2^{J}, centered on zero, where a reasonably good guess for J𝐽J can be obtained from the model characteristic function cumulants. In the evaluation of a single option strike, the cost of computing the payoff coefficients will dominate the cost of evaluating the price based on the sum of the Vm,ksubscript𝑉

𝑚𝑘V\_{m,k} multiplied by the (precomputed) density coefficients cm,ksubscript𝑐

𝑚𝑘c\_{m,k}. Furthermore, the number of coefficients must be a power of two and must include [k1,k2)subscript𝑘1subscript𝑘2[k\_{1},k\_{2}).

The scale m𝑚m is more challenging to guess. It can be guessed from the rule used to truncate the integral of the more standard Fourier based approach from Andersen and
Piterbarg [[2](#bib.bib2)], refined in [[7](#bib.bib7)]. It then directly depends on the asymptotic behaviour of the characteristic function. Maree
et al. [[11](#bib.bib11)] propose a simple iterative method to determine n𝑛n automatically (with very few iterations on m𝑚m).

## 8 Numerical examples

### 8.1 Payoff coefficients Vm,ksubscript𝑉 𝑚𝑘V\_{m,k} and the FFT

Vieta’s formula is not very efficient to compute a single coefficient Vm,ksubscript𝑉

𝑚𝑘V\_{m,k} but as we compute close to 2Jsuperscript2𝐽2^{J} coefficients the FFT improves its performance significantly. For 21​0superscript2102^{1}0 coefficients, Vieta’s formula end up around six times faster than the CERN algorithm.

Table 2: Time in microseconds taken to compute Vm,ksubscript𝑉

𝑚𝑘V\_{m,k} for k=0,…,2J−1−1𝑘

0…superscript2𝐽11k=0,...,2^{J-1}-1 with m=6𝑚6m=6, a=−1𝑎1a=-1.

| J𝐽J | FFT | CERN |
| --- | --- | --- |
| 5 | 1.7 | 10.7 |
| 10 | 56 | 360 |

While the raw difference in performance is impressive. It is more interesting to look at the actual performance difference when pricing vanilla Put options under the Heston stochastic volatility model. We consider two different Heston parameter sets for two distinct option maturities. This leads to two vastly different truncation ranges [a,b]𝑎𝑏[a,b], computed according to the Heston cumulants. As a result 2J=212=k2−k1superscript2𝐽superscript212subscript𝑘2subscript𝑘12^{J}=2^{12}=k\_{2}-k\_{1} for the first set and 2J=28=k2−k1superscript2𝐽superscript28subscript𝑘2subscript𝑘12^{J}=2^{8}=k\_{2}-k\_{1} for the second set. Ignoring the initialization time where the cm,ksubscript𝑐

𝑚𝑘c\_{m,k} are computed, which needs to be done only once per option expiry, the direct CERN algorithm is between five to eight times slower.

Table 3: Heston parameter sets.

| Name | v0subscript𝑣0v\_{0} | κ𝜅\kappa | θ𝜃\theta | σ𝜎\sigma | ρ𝜌\rho | F𝐹F | T𝑇T |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Set 1 | 0.1 | 1.0 | 0.1 | 1.0 | -0.9 | 1.0 | 2 days |
| Set 2 | 0.0225 | 0.1 | 0.01 | ,2.0 | 0.5 | 1000000 | 1 year |




Table 4: Time in milliseconds taken to compute the Put option price under two different Heston parameter sets.

| Heston | Method | Price | Error | Time (ms) |
| --- | --- | --- | --- | --- |
| Set 1 (J=12) | FFT | 117.9149 | -1.4704 | 0.250 |
|  | CERN | 117.9144 | -1.4708 | 1.370 |
| Set 2 (J=8) | FFT | 0.006361 | -3.49e-15 | 0.016 |
|  | CERN | 0.006361 | 6.42e-13 | 0.101 |

### 8.2 New payoff coefficients versus the original formulation

We consider options of maturity 2 days (short) in order to make the issue more visible and we consider the Heston parameters s κ=1.0,θ=0.1,σ=1.0,ρ=−0.9,v0=0.1formulae-sequence𝜅1.0formulae-sequence𝜃0.1formulae-sequence𝜎1.0formulae-sequence𝜌0.9subscript𝑣00.1\kappa=1.0,\theta=0.1,\sigma=1.0,\rho=-0.9,v\_{0}=0.1, along with a forward price at valuation time F=1.0𝐹1.0F=1.0. Those parameters are not extreme, and are in the typical range of a Heston fits to market option prices.

In Figure [1](#S8.F1 "Figure 1 ‣ 8.2 New payoff coefficients versus the original formulation ‣ 8 Numerical examples ‣ Notes on the SWIFT method based on Shannon Wavelets for Option Pricing"), we look at the absolute error in price for a scale m=8𝑚8m=8 and a truncation L=12𝐿12L=12 based on the Heston cumulants. This truncation corresponds to an interval [a,b]=[−0.2815,0.2810]𝑎𝑏0.28150.2810[a,b]=[-0.2815,0.2810]. Our reference is the price obtained by the Lord-Kahl optimal alpha method Lord and Kahl [[8](#bib.bib8)]. We consider two ways of computing the payoff coefficients: the classic payoff formula of [[12](#bib.bib12)] represented by equation ([25](#S5.E25 "In 5 Alternative payoff coefficients ‣ Notes on the SWIFT method based on Shannon Wavelets for Option Pricing")), and our new formula represented by equation ([23](#S5.E23 "In 5 Alternative payoff coefficients ‣ Notes on the SWIFT method based on Shannon Wavelets for Option Pricing")). We make sure that the density coefficients are computed with maximum accuracy by using a large J𝐽J, so that the overall error is dominated by error in the payoff formula.

Figure 1: Error in Vanilla option prices of maturity 2 days with Heston parameters κ=1.0,θ=0.1,σ=1.0,ρ=−0.9,v0=0.1,F=1.0formulae-sequence𝜅1.0formulae-sequence𝜃0.1formulae-sequence𝜎1.0formulae-sequence𝜌0.9formulae-sequencesubscript𝑣00.1𝐹1.0\kappa=1.0,\theta=0.1,\sigma=1.0,\rho=-0.9,v\_{0}=0.1,F=1.0 using a truncation levels L=12𝐿12L=12 and scale m=8𝑚8m=8.

![Refer to caption](/html/2005.13252/assets/x1.png)

We stop at strike K=1.32𝐾1.32K=1.32 since then ln⁡KF>b𝐾𝐹𝑏\ln\frac{K}{F}>b. Figure [1](#S8.F1 "Figure 1 ‣ 8.2 New payoff coefficients versus the original formulation ‣ 8 Numerical examples ‣ Notes on the SWIFT method based on Shannon Wavelets for Option Pricing") shows that the error of the new formula stays below 10−13superscript101310^{-13}, close to machine epsilon while the error of the classic formula can be as high as 1.5⋅10−2⋅1.5superscript1021.5\cdot 10^{-2} when the strike approaches the upper boundary F​eb𝐹superscript𝑒𝑏Fe^{b}.

### 8.3 Density coefficients cm,ksubscript𝑐 𝑚𝑘c\_{m,k} and quadratures

We consider the same Heston model parameters as in the previous section. The trapezoidal rule is three to six times more accurate than the mid-point rule (or equivalently the formula from Ortiz-Gracia and
Oosterlee [[12](#bib.bib12)] based Vieta’s formula) across strikes and on both Heston sets. Both rules use exactly the same number of points.

Table 5: Price of an out-of-the-money option under two different Heston parameter sets.

| Heston | Method | Strike | Price | Error |
| --- | --- | --- | --- | --- |
| Set 1 (m=8,J=12formulae-sequence𝑚8𝐽12m=8,J=12) | Midpoint | 250000 | 114.51 | -4.87 |
|  | Trapezoidal | 250000 | 117.91 | -1.47 |
|  | Midpoint | 4000000 | 3866.59 | -85.33 |
|  | Trapezoidal | 4000000 | 3931.09 | -20.82 |
| Set 2 (m=6,J=5formulae-sequence𝑚6𝐽5m=6,J=5) | Midpoint | 1.0064 | 0.0063611 | 3.97e-07 |
|  | Trapezoidal | 1.0064 | 0.0063606 | -7.39e-08 |
|  | Midpoint | 1.064 | 4.77e-06 | 5.09e-07 |
|  | Trapezoidal | 1.064 | 4.18e-06 | -8.22e-08 |

We now look at the time to initialize the SWIFT method for a given option maturity. This corresponds to the calculation of the density coefficients cm,ksubscript𝑐

𝑚𝑘c\_{m,k}, either with the FFT applied on the trapezoidal quadrature, or with the direct adaptive Filon quadrature on a relative tolerance of 10−8superscript10810^{-8} (which leads to a similar accuracy as the FFT approach).

Table 6: Initialization time of the SWIFT method for two different Heston parameter sets and different quadratures.

| Heston | Method | Points | Time (microseconds) |
| --- | --- | --- | --- |
| Set 1 | FFT | 4096 | 433 |
|  | Filon | 585 | 76000 |
| Set 2 | FFT | 32 | 16 |
|  | Filon | 497 | 588 |

For a similar accuracy, the initialization based on the adaptive Filon quadrature is slower by a factor of more than 32 although the characteristic function is evaluated 585 times compared to 2048 times for the FFT calculation. There is then a lot of room if we were to make the FFT density calculation adaptive by doubling successively the interval [k1,k2]subscript𝑘1subscript𝑘2[k\_{1},k\_{2}].

## 9 Conclusion

The use of the fast Fourier transform (FFT) to compute the payoff coefficients is particularly important and makes the SWIFT method competitive with some of the fastest pricing methods such as COS method of Fang and Oosterlee [[3](#bib.bib3)]. Our alternative formula centered on the forward is more accurate in general than the original payoff coefficients formula from Ortiz-Gracia and
Oosterlee [[12](#bib.bib12)] while being of equivalent computational cost.

The calculation of the density coefficients also benefits from the FFT, even though the related characteristic function is relatively expensive to compute. The FFT based on the trapezoidal rule is much more accurate than the original formula from Ortiz-Gracia and
Oosterlee [[12](#bib.bib12)] for a slightly lower computational cost. Using more fancy adaptive quadratures is no so useful.
A simple adaptive scheme based successively doubling the truncation interval [k1,k2]subscript𝑘1subscript𝑘2[k\_{1},k\_{2}] according to the accuracy of the area underneath the curve is good enough.

## References

* Amos [1990]

  Amos, D. E. (1990) Algorithms 683: a portable FORTRAN subroutine for
  exponential integrals of a complex argument, ACM Transactions on
  Mathematical Software (TOMS), 16(2), pp. 178–182.
* Andersen and
  Piterbarg [2010]

  Andersen, L. B. and Piterbarg, V. V. (2010) Interest Rate Modeling,
  Volume I: Foundations and Vanilla Models, (Atlantic Financial Press
  London).
* Fang and Oosterlee [2008]

  Fang, F. and Oosterlee, C. W. (2008) A novel pricing method for European
  options based on Fourier-cosine series expansions, SIAM Journal on
  Scientific Computing, 31(2), pp. 826–848.
* Jin and Jjie [1996]

  Jin, J. and Jjie, Z. S. (1996) Computation of special functions,
  (Wiley).
* Johnson [2011]

  Johnson, S. G., Numerical integration and the redemption of the trapezoidal
  rule. (2011) , Technical report, MIT Applied Math.
* Kölbig [1990]

  Kölbig, K., Exponential Integral for Complex Argument. (1990) , Technical
  report, CERN.
* Le Floc’h [2013]

  Le Floc’h, F. (2013) Fourier Integration and Stochastic Volatility
  Calibration, Available at SSRN 2362968.
* Lord and Kahl [2007]

  Lord, R. and Kahl, C. (2007) Optimal Fourier inversion in semi-analytical
  option pricing, SSRN papers.ssrn.com/abstract=921336.
* MacLeod [1996]

  MacLeod, A. J. (1996) Rational approximations, software and test methods for
  sine and cosine integrals, Numerical Algorithms, 12(2), pp.
  259–272.
* Makhoul [1980]

  Makhoul, J. (1980) A fast cosine transform in one and two dimensions, IEEE Transactions on Acoustics, Speech, and Signal Processing, 28(1), pp.
  27–34.
* Maree
  et al. [2017]

  Maree, S. C., Ortiz-Gracia, L. and Oosterlee, C. W. (2017) Pricing
  early-exercise and discrete barrier options by Shannon wavelet expansions,
  Numerische Mathematik, 136(4), pp. 1035–1070.
* Ortiz-Gracia and
  Oosterlee [2016]

  Ortiz-Gracia, L. and Oosterlee, C. W. (2016) A highly efficient Shannon wavelet
  inverse Fourier technique for pricing European options, SIAM
  Journal on Scientific Computing, 38(1), pp. B118–B143.
* Pegoraro and
  Slusallek [2011]

  Pegoraro, V. and Slusallek, P. (2011) On the evaluation of the complex-valued
  exponential integral, Journal of Graphics, GPU, and Game Tools,
  15(3), pp. 183–198.
* Trefethen and
  Weideman [2014]

  Trefethen, L. N. and Weideman, J. (2014) The exponentially convergent
  trapezoidal rule, SIAM Review, 56(3), pp. 385–458.

## Appendix A Computing the discrete Cosine and Sine transforms together from the FFT

The calculation of the Vm,ksubscript𝑉

𝑚𝑘V\_{m,k} by the formula described in Appendix A of Ortiz-Gracia and
Oosterlee [[12](#bib.bib12)] is the sum of a type 2 discrete cosine transform (DCT) and a type 2 discrete sine transform (DST). It can be summarized by the following equation

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vm,ksubscript𝑉  𝑚𝑘\displaystyle V\_{m,k} | =∑j=0N−1aj​cos⁡(π​k​j+12N)+bj​sin⁡(π​k​j+12N)absentsuperscriptsubscript𝑗0𝑁1subscript𝑎𝑗𝜋𝑘𝑗12𝑁subscript𝑏𝑗𝜋𝑘𝑗12𝑁\displaystyle=\sum\_{j=0}^{N-1}a\_{j}\cos\left(\pi k\frac{j+\frac{1}{2}}{N}\right)+b\_{j}\sin\left(\pi k\frac{j+\frac{1}{2}}{N}\right) |  | (35) |

with N=2J¯−1𝑁superscript2¯𝐽1N=2^{\bar{J}-1} for some positive integer J¯¯𝐽\bar{J}.
Makhoul [[10](#bib.bib10)] gives a simple algorithm to compute the DCT of size N𝑁N with one FFT of size N𝑁N.
We simply initialize the FFT coefficients cjsubscript𝑐𝑗c\_{j} with:

|  |  |  |  |
| --- | --- | --- | --- |
|  | cj=a2​j,cN−1−j=a2​j+1 for j=0,…,N2−1c\_{j}=a\_{2j}\quad\,,\quad c\_{N-1-j}=a\_{2j+1}\quad\textmd{ for }j=0,...,\frac{N}{2}-1 |  | (36) |

and then from the result of the FFT c^^𝑐\hat{c}, the DCT coefficients a^^𝑎\hat{a} are

|  |  |  |  |
| --- | --- | --- | --- |
|  | a^k=ℜ⁡[c^j​e−i​π​k2​N]subscript^𝑎𝑘subscript^𝑐𝑗superscript𝑒𝑖𝜋𝑘2𝑁\hat{a}\_{k}=\Re\left[\hat{c}\_{j}e^{-i\pi\frac{k}{2N}}\right] |  | (37) |

Makhoul does not specify the equivalent formula for the DST, but we can do something similar. We first initialize the FFT coefficients cjsubscript𝑐𝑗c\_{j} with:

|  |  |  |  |
| --- | --- | --- | --- |
|  | cj=b2​j,cN−1−j=−b2​j+1 for j=0,…,N2−1c\_{j}=b\_{2j}\quad\,,\quad c\_{N-1-j}=-b\_{2j+1}\quad\textmd{ for }j=0,...,\frac{N}{2}-1 |  | (38) |

and then from the result of the FFT c^^𝑐\hat{c}, the DST coefficients b^^𝑏\hat{b} are

|  |  |  |  |
| --- | --- | --- | --- |
|  | b^k=−ℑ⁡[c^j​e−i​π​k2​N]subscript^𝑏𝑘subscript^𝑐𝑗superscript𝑒𝑖𝜋𝑘2𝑁\hat{b}\_{k}=-\Im\left[\hat{c}\_{j}e^{-i\pi\frac{k}{2N}}\right] |  | (39) |

For maximum performance, the two FFTs can reuse the same sine and cosine tables. And the last step of the DCT and DST can be combined together.

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/2005.13252)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2005.13252)
[View original  
on arXiv](https://arxiv.org/abs/2005.13252)[►](javascript: void(0))