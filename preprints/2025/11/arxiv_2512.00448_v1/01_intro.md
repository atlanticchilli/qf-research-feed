---
authors:
- Changqing Teng
- Guanglian Li
doc_id: arxiv:2512.00448v1
family_id: arxiv:2512.00448
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Efficient Calibration in the rough Bergomi model by Wasserstein distance
url_abs: http://arxiv.org/abs/2512.00448v1
url_html: https://arxiv.org/html/2512.00448v1
venue: arXiv q-fin
version: 1
year: 2025
---

RMSE
MAE
MAPE
MaxAPE
RMSE
MAE
MAPE
MaxAPE

ξ0(1)​(t)\xi\_{0}^{(1)}(t)
PWC-8
14.0561
172
8.7270e-5
7.0621e-5
0.0046
0.0150


NS
13.8007
596
0.0002
0.0001
0.0116
0.0667
0.0017
0.0015
0.0543
0.1455


NS+NN
13.8025
643
0.0002
0.0001
0.0116
0.0661
0.0017
0.0015
0.0536
0.1435

ξ0(2)​(t)\xi\_{0}^{(2)}(t)
PWC-8
13.8567
1069
0.0004
0.0003
0.0063
0.0230


NS
14.0246
3188
0.0002
0.0002
0.0027
0.0099
0.0015
0.0013
0.0153
0.0335


NS+NN
13.8616
1048
0.0003
0.0002
0.0042
0.0142
0.0026
0.0024
0.0277
0.0554

ξ0(3)​(t)\xi\_{0}^{(3)}(t)
PWC-8
14.0446
99
0.0001
0.0001
0.0037
0.0108


NS
14.2029
245
0.0002
0.0002
0.0097
0.0393
0.0018
0.0018
0.0358
0.0590


NS+NN
14.2072
260
0.0002
0.0002
0.0096
0.0390
0.0018
0.0017
0.0354
0.0582

Table 12: The performance comparison between different parameterizations of the initial forward variance curve.

![Refer to caption](Figure/xi0_calibration_comparison.png)


Figure 10: The calibrated ξ0​(t)\xi\_{0}(t) using different parameterizations.

## 5 Conclusion

This work introduced a comprehensive framework that addresses the dual challenges of efficient pricing and robust calibration in the rough Bergomi model.

First, we developed a modified Sum-of-Exponentials (mSOE) Monte Carlo scheme by hybridizing an exact treatment of the kernel singularity at the origin with a high-fidelity sum-of-exponentials approximation for the remainder. Our method achieves stable convergence and high accuracy, particularly for out-of-the-money options, compared with the SOE scheme. It maintains an 𝒪​(n)\mathcal{O}(n) computational complexity, which makes it a practical and efficient pricing engine.

Second, we proposed a novel calibration paradigm based on distributional matching via the Wasserstein-1 distance, which minimizes the distance between the model-generated and market-implied risk-neutral distributions. It provides a uniform bound on pricing errors over all strikes and corresponds to an adversarial optimization over Lipschitz payoffs. Extensive numerical tests confirm that this framework yields superior parameter identifiability and exceptional generalization capability to exotic options such as barrier options, compared to the traditional mean squared error approach. The ”simulate-and-compare” paradigm, enabled by our efficient mSOE pricer, makes this a generic and powerful tool for calibrating complex models where fast analytical pricing is unavailable.

Finally, we demonstrated the flexibility of the calibration framework by incorporating different parameterizations for the initial forward variance curve ξ0​(t)\xi\_{0}(t). This allows the model to adapt to various term structure shapes present in market data.

Future work will focus on several promising directions. The most immediate extension is the application of our framework to real market data. This involves extracting the market-implied risk-neutral distribution from option price quotes to compute the empirical Wasserstein distance. Furthermore, the generic nature of our calibration framework invites its application to other rough and non-Markovian models beyond rBergomi.

## Acknowledgements

GL acknowledges the support from GRF (project number: 17317122) and the Early Career Scheme (Project number: 27301921), RGC, Hong Kong.

## References

* [1]

  M. Abadi, P. Barham, J. Chen, Z. Chen, A. Davis, J. Dean, M. Devin,
  S. Ghemawat, G. Irving, M. Isard, et al.
  Tensorflow: a system for large-scale machine learning.
  In 12th USENIX symposium on operating systems design and
  implementation (OSDI 16), pages 265–283, 2016.
* [2]

  E. Abi Jaber and O. El Euch.
  Multifactor approximation of rough volatility models.
  SIAM Journal on Financial Mathematics, 10(2):309–349, 2019.
* [3]

  F. Baschetti, G. Bormetti, and P. Rossi.
  Deep calibration with random grids.
  Quantitative Finance, pages 1–23, 2024.
* [4]

  C. Bayer and S. Breneis.
  Markovian approximations of stochastic Volterra equations with the
  fractional kernel.
  Quantitative Finance, 23(1):53–70, 2023.
* [5]

  C. Bayer and S. Breneis.
  Weak Markovian approximations of rough Heston.
  arXiv preprint arXiv:2309.07023, 2023.
* [6]

  C. Bayer, P. Friz, and J. Gatheral.
  Pricing under rough volatility.
  Quantitative Finance, 16(6):887–904, 2016.
* [7]

  M. Bennedsen, A. Lunde, and M. S. Pakkanen.
  Hybrid scheme for Brownian semistationary processes.
  Finance and Stochastics, 21:931–965, 2017.
* [8]

  D. Braess.
  Nonlinear approximation theory.
  Springer Science & Business Media, 2012.
* [9]

  M. De Angelis and A. Gray.
  Why the 1-Wasserstein distance is the area between the two marginal
  cdfs.
  arXiv preprint arXiv:2111.03570, 2021.
* [10]

  T. DeLise.
  Neural options pricing.
  Preprint, arXiv:2105.13320, 2021.
* [11]

  S. Figlewski.
  Risk-neutral densities: A review.
  Annual Review of Financial Economics, 10(1):329–359, 2018.
* [12]

  P. Gassiat.
  On the martingale property in the rough Bergomi model.
  2019.
* [13]

  J. Gatheral, T. Jaisson, and M. Rosenbaum.
  Volatility is rough.
  In Commodities, pages 659–690. Chapman and Hall/CRC, 2022.
* [14]

  A. Gulisashvili.
  Gaussian stochastic volatility models: Scaling regimes, large
  deviations, and moment explosions.
  Stochastic Processes and their Applications, 130(6):3648–3686,
  2020.
* [15]

  P. Harms.
  Strong convergence rates for Markovian representations of
  fractional Brownian motion, 2019.
* [16]

  B. Horvath, A. Muguruza, and M. Tomas.
  Deep learning volatility: a deep neural network perspective on
  pricing and calibration in (rough) volatility models.
  Quantitative Finance, 21(1):11–27, 2021.
* [17]

  S. Jiang, J. Zhang, Q. Zhang, and Z. Zhang.
  Fast evaluation of the Caputo fractional derivative and its
  applications to fractional diffusion equations.
  Communications in Computational Physics, 21(3):650–678, 2017.
* [18]

  P. Kidger, J. Foster, X. Li, and T. J. Lyons.
  Neural SDEs as infinite-dimensional GANs.
  In International conference on machine learning, pages
  5453–5463. PMLR, 2021.
* [19]

  S. Liu, A. Borovykh, L. A. Grzelak, and C. W. Oosterlee.
  A neural network-based framework for financial model calibration.
  Journal of Mathematics in Industry, 9(1):9, 2019.
* [20]

  C. R. Nelson and A. F. Siegel.
  Parsimonious modeling of yield curves.
  Journal of business, pages 473–489, 1987.
* [21]

  S. E. Rømer.
  Hybrid multifactor scheme for stochastic Volterra equations with
  completely monotone kernels.
  Available at SSRN 3706253, 2022.
* [22]

  A. Tong, T. Nguyen-Tang, T. Tran, and J. Choi.
  Learning fractional white noises in neural stochastic differential
  equations.
  In Advances in Neural Information Processing Systems,
  volume 35, pages 37660–37675, 2022.
* [23]

  C. Villani.
  Topics in optimal transportation.
  American Mathematical Soc., Providence, 2021.
* [24]

  D. V. Widder.
  The Laplace Transform, volume vol. 6 of Princeton
  Mathematical Series.
  Princeton University Press, Princeton, NJ, 1941.
* [25]

  Q. Zhu, G. Loeper, W. Chen, and N. Langrené.
  Markovian approximation of the rough Bergomi model for Monte
  Carlo option pricing.
  Mathematics, 9(5):528, 2021.