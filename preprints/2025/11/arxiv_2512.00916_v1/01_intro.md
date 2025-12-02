---
authors:
- Sotirios D. Nikolopoulos
doc_id: arxiv:2512.00916v1
family_id: arxiv:2512.00916
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts
url_abs: http://arxiv.org/abs/2512.00916v1
url_html: https://arxiv.org/html/2512.00916v1
venue: arXiv q-fin
version: 1
year: 2025
---


Sotirios D. Nikolopoulos
Department of Accounting and Finance, University of Peloponnese, Greece
[s.nikolopoulos@go.uop.gr](mailto:s.nikolopoulos@go.uop.gr)

###### Abstract

Evaluating rare-event forecasts is challenging because standard metrics collapse as event prevalence declines. Measures such as F1-score, AUPRC, MCC, and accuracy induce degenerate thresholds—converging to zero or one—and their values become dominated by class imbalance rather than tail discrimination. We develop a family of rare-event-stable (RES) metrics whose optimal thresholds remain strictly interior as the event probability approaches zero, ensuring coherent decision rules under extreme rarity. Simulations spanning event probabilities from 0.01 down to one in a million show that RES metrics maintain stable thresholds, consistent model rankings, and near-complete prevalence invariance, whereas traditional metrics exhibit statistically significant threshold drift and structural collapse. A credit-default application confirms these results: RES metrics yield interpretable probability-of-default cutoffs (4–9%) and remain robust under subsampling, while classical metrics fail operationally. The RES framework provides a principled, prevalence-invariant basis for evaluating extreme-risk forecasts.

###### keywords:

Rare events, Classification, Decision analysis, Proper scoring rules, Early warning systems

## 1 Introduction

Forecasting rare events is fundamental in credit risk, crisis prediction, fraud detection, and safety engineering. In such settings, the prevalence of positive outcomes may lie orders of magnitude below conventional levels, yet the cost of missed detections remains substantial. Although probability forecasting methods have advanced rapidly, the evaluation of these forecasts remains challenging: widely used performance metrics behave inconsistently as prevalence declines, often producing unstable or operationally difficult-to-justify decision thresholds.

A central observation motivating this paper is that traditional threshold-based metrics such as the F1-score, MCC, and Balanced Accuracy embed marginal trade-offs that depend implicitly on the event prevalence π\pi. As π→0\pi\to 0, these implicit trade-offs diverge, forcing the induced optimal thresholds toward extreme values even when the underlying predictive model remains unchanged. This threshold-collapse mechanism has been noted empirically but has lacked a general theoretical explanation. As rarity increases, these metrics increasingly obscure meaningful differences in tail discrimination precisely where reliable operational decision-making depends on stable threshold behaviour.

We address this gap by developing a class of Rare-Event-Stable (RES) performance metrics that remain well behaved under extreme rarity. These metrics introduce a policy parameter α\alpha that reflects the institution’s relative tolerance for false positives and false negatives. Crucially, α\alpha is a stable preference parameter, while the implementation threshold δ∗\delta^{\ast} remains a data-driven quantity. This separation enables coherent and interpretable decision-making across models, samples, and prevalence regimes.

#### Contributions

This paper makes four primary contributions to the evaluation of rare-event classification. First, we provide an analytical explanation for the structural instabilities exhibited by common metrics such as the F1-score, MCC, and Balanced Accuracy, and we document these instabilities empirically across a wide range of prevalence conditions. Second, we develop a general class of RES metrics based on a prevalence-invariant policy parameter α\alpha that separates stable institutional preferences from the data-driven determination of δ∗\delta^{\ast}. Third, we propose practical calibration procedures that map historical operating policies, capacity constraints, and explicit loss structures into a transparent and interpretable choice of α\alpha. Fourth, through large-scale simulations and an empirical application to credit-default forecasting, we show that RES metrics yield interior, stable, and economically interpretable thresholds even under extreme rarity, in contrast to the degeneracy observed in traditional performance measures.

The remainder of the paper is organised as follows. Section [2](https://arxiv.org/html/2512.00916v1#S2 "2 Literature Review and Conceptual Framework ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts") reviews the literature and conceptual framework. Section [3](https://arxiv.org/html/2512.00916v1#S3 "3 Decision-Theoretic Foundations ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts") establishes the decision-theoretic foundations, motivating the RES metrics introduced in Section [4](https://arxiv.org/html/2512.00916v1#S4 "4 Rare-Event-Stable Metrics ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts"). The asymptotic behaviour is derived in Section [5](https://arxiv.org/html/2512.00916v1#S5 "5 Asymptotic Behavior and Robustness Conditions ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts"), followed by simulation and empirical results in Sections [6](https://arxiv.org/html/2512.00916v1#S6 "6 Simulation Design and Results ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts") and [7](https://arxiv.org/html/2512.00916v1#S7 "7 Application: Credit-Default Forecasting Under Extreme Rarity ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts"). Technical proofs, detailed experimental protocols, calibration procedures, and extensive supplementary diagnostics are provided in Appendices A–J.

## 2 Literature Review and Conceptual Framework

Forecast evaluation for rare events lies at the intersection of several established strands of research: the theory of proper scoring rules and probabilistic evaluation, the extensive literature on class imbalance and rare-event modelling, and the operational practice of threshold-based alarm systems used in supervisory and risk-management environments. Although these literatures are often connected implicitly in applied work, their combined implications for decision-making under extreme rarity have received comparatively little theoretical scrutiny. This section synthesizes these strands, identifies the conceptual gap that motivates our contribution, and develops the framework underlying the RES approach.

The formal evaluation of probability forecasts typically relies on proper scoring rules such as the Brier score and the logarithmic score (gneiting2007strictly; gneiting2011comparing). These criteria are theoretically attractive because they reward full-distribution accuracy and align with Bayesian decision theory under well-specified loss functions. However, by integrating performance over the entire distribution, proper scoring rules may underweight tail behaviour, a concern raised repeatedly in risk-management and macroeconomic forecasting contexts. Studies such as diks2011likelihood emphasise the importance of examining tail behaviour explicitly, while lahiri2013evaluating show that standard evaluation techniques can fail to capture economic value under asymmetric loss. Experimental evidence further indicates that forecasters implicitly recognise increased tail uncertainty by widening prediction intervals in the extremes (sonsino2025decrease). These observations highlight the distinction between full-distribution evaluation and the threshold-based decisions that govern operational intervention.

Alongside this literature, a broad methodological effort has sought to address the modelling
challenges associated with rare events and severe class imbalance. Research in credit risk
(antunes2018forecasting; brownlees2015srisk; dinnocenzo2024modeling), fraud detection (hernandez2024financial; ngai2011application), anomaly detection (breunig2000lof; wang2020deep), and early-warning systems (candelon2014currency) has produced numerous strategies to mitigate imbalance, including resampling techniques such as SMOTE (chawla2002smote; he2009learning), rare-event correction to logistic regression (king2001logistic), and imbalance-aware learning algorithms (lin2017focal). Yet despite significant methodological progress, evaluation practice often relies on metrics whose structural behaviour under extreme imbalance remains poorly understood. The general limitations of F-measures and correlation-based metrics have been widely discussed
(e.g., powers2011evaluation; flach2015precision; saito2015precision; davis2006relationship),
and recent analytical work (minus2025behavior) demonstrates that such metrics may behave
unpredictably as the event probability becomes very small. These findings reinforce the need for
evaluation criteria whose optimisation behaviour remains stable and interpretable in the rare-event limit.

The operational literature on threshold selection and alarm systems provides additional insight. Threshold rules in credit supervision, systemic-risk monitoring, fraud screening, and safety engineering commonly rely on ROC analysis, Youden’s index (youden1950index), and cost-sensitive classification frameworks (hand2009measuring; hand2010proper; drummond2006roc). This literature recognises that threshold choice must reflect an institution’s tolerance for false positives versus false negatives, and that such tolerances are often asymmetric in high-stakes settings. Echoing this view, tetlock2023false, drawing on taleb2022single (taleb2022single), argues that meaningful alarm policies require marginal trade-offs that reflect policymaker risk preferences rather than numerical artefacts of imbalance.

Two empirical regularities emerge across these literatures. First, traditional classification metrics exhibit systematic instability as prevalence declines. Their implicit marginal penalties for false positives and false negatives vary systematically with prevalence, even when the underlying decision costs are intended to be prevalence-invariant. Empirical studies have consistently documented threshold drift, volatility, and degradation of discriminative resolution (flach2015precision; saito2015precision; davis2006relationship). The recent M6 forecasting competition (makridakis2025m6) reinforces this point: even highly accurate probability forecasts can lead to poor operational decisions when the evaluation metric is misaligned with the decision environment. Second, despite extensive research on class imbalance, no widely used metric provides a structural guarantee of threshold stability as π→0\pi\to 0; most either collapse to boundary thresholds or lose discriminative power, raising concerns about their suitability for operational use.

Taken together, these findings reveal a conceptual gap: while much is known about modelling rare events and about evaluating full probability forecasts, relatively little is known about the structural behaviour of threshold-based metrics under extreme rarity. The central premise motivating our contribution is that threshold-based metrics must remain well behaved as prevalence declines; otherwise, they cannot support coherent or defensible decision policies. The RES framework introduced in the next section addresses this gap by formalizing a class of metrics whose marginal trade-offs remain stable as π→0\pi\to 0, ensuring interior thresholds and consistent rankings across prevalence regimes.

The following section formalizes these requirements and develops the structural conditions for rare-event stability.

## 3 Decision-Theoretic Foundations

Forecast evaluation in rare-event environments ultimately reduces to a decision problem: whether a probabilistic forecast should trigger an alarm. Institutions observing a probability estimate η​(x)\eta(x) must specify a threshold δ∈[0,1]\delta\in[0,1] and intervene whenever η​(x)≥δ\eta(x)\geq\delta. The practical value of any evaluation metric therefore depends not only on its numerical score but on the behaviour of the metric-induced optimal threshold,

|  |  |  |
| --- | --- | --- |
|  | δ∗=arg⁡maxδ∈[0,1]⁡𝔼​[M​(δ;Y,η​(X))],\delta^{\ast}=\arg\max\_{\delta\in[0,1]}\mathbb{E}[M(\delta;Y,\eta(X))], |  |

whose properties determine how probabilistic forecasts are translated into operational actions. This section develops the decision-theoretic foundations for analysing δ∗\delta^{\ast} in the asymptotic regime where the event probability π=Pr⁡(Y=1)\pi=\Pr(Y=1) becomes vanishingly small. We show that many widely used metrics become structurally incompatible with coherent alarm systems as prevalence declines, and we use this insight to motivate the rare-event-stable (RES) framework developed in the next section.

Alarm thresholds play a central role in credit regulation, early-warning systems, fraud detection, and systemic-risk surveillance. For a performance metric to guide decisions in such environments, its induced threshold must satisfy two essential coherence requirements. First, the threshold must remain well defined and unique across similar environments; metrics whose maximising thresholds oscillate between extreme values produce inconsistent and operationally meaningless alarm behaviour. Second, the threshold must evolve predictably as prevalence changes. Institutions routinely operate under shifting baseline risks, and an evaluation criterion that produces erratic or discontinuous threshold movements as π\pi declines cannot support stable policy or risk-management decisions.

These considerations become particularly salient in the rare-event limit, where we consider asymptotic sequences in which π→0\pi\to 0 while the conditional forecast distribution remains fixed. This framework captures practical environments where events occur with probabilities far below one percent, including credit defaults in high-quality portfolios, severe system failures, and geopolitical tail risks. Two conditions are necessary for meaningful evaluation in this limit.

#### Condition C1: Bounded Optimal Thresholds

A metric must produce an optimal threshold δ∗\delta^{\ast} that remains strictly interior as π→0\pi\to 0. Thresholds that collapse to 0 or 11 are operationally uninformative, since they correspond to always-alarm or never-alarm rules regardless of the model’s discriminatory content. Boundedness ensures that the metric continues to operate in the region of the score distribution where meaningful discrimination is possible.

#### Condition C2: Stable Model Rankings

A metric must preserve the ordering of models as prevalence declines. If one model provides stronger upper-tail discrimination than another, the evaluation criterion must continue to reflect this as events become rarer, rather than allowing prevalence effects to dominate the metric’s behaviour.

The structure of traditional metrics explains why these coherence requirements often fail. Metrics built from confusion-matrix components depend on TPR​(δ)\mathrm{TPR}(\delta) and FPR​(δ)\mathrm{FPR}(\delta), and their expected value can be expressed as a function of these quantities and of π\pi. When π\pi is small, terms weighted by (1−π)(1-\pi) dominate, meaning that the contribution of the negative class overwhelms that of the positive class. This imbalance causes many metrics to overweight the penalty for false positives: as prevalence declines, the marginal trade-off embedded in the metric shifts toward avoiding false alarms, forcing the optimal threshold toward the upper boundary regardless of the underlying signal strength. This mechanism is not a sampling artifact but a structural feature of the metric’s functional form.

This observation explains the systematic collapse of widely used metric families. Precision–recall measures such as the F1-score deteriorate because precision scales with π\pi in a way that becomes negligible as π→0\pi\to 0, producing conflicting optimisation pressures that push the threshold toward either 0 or 11 depending on the distributional tails. Correlation-based metrics such as the Matthews Correlation Coefficient incorporate multiplicative π​(1−π)\sqrt{\pi(1-\pi)} terms that force the maximising threshold toward 11, effectively implementing a never-alarm rule even when models exhibit strong discriminatory power. The Area Under the ROC Curve, though threshold-free, becomes uninformative in the rare-event limit because ROC geometry is insensitive to prevalence; AUC saturates near unity and loses the ability to discriminate between models with materially different tail behaviour. Conventional accuracy measures behave similarly: as π→0\pi\to 0, accuracy converges to the true negative rate, systematically ignoring the ability to detect rare events unless misclassification costs are explicitly rescaled with prevalence.

These pathologies highlight the necessity of threshold boundedness in extreme-risk environments. A metric is rare-event-stable if its induced threshold remains strictly interior as π→0\pi\to 0, thereby continuing to operate in the region of the score distribution where meaningful discrimination between rare events and non-events occurs. Metrics failing this condition cannot support consistent operational interpretation, as their induced decision rules collapse when prevalence becomes small.

One might argue that threshold collapse is optimal under standard Bayesian decision theory with fixed misclassification costs, since the Bayes-optimal threshold depends directly on π\pi. However, many high-stakes environments differ markedly from this classical setting. In systemic-risk monitoring, missing a single important event carries consequences far exceeding those implied by constant misclassification costs; in credit regulation, defaults in high-quality portfolios trigger supervisory attention independently of their base rate; and in reliability engineering, rare failures often entail non-linear losses. In such environments, the effective false-negative cost increases as the event becomes rarer, scaling approximately as 1/π1/\pi. Under this structure, the decision-theoretic optimum coincides with the rare-event-stable regime. The RES framework formalises this institutional reality by embedding prevalence-invariant marginal trade-offs through a policy parameter α\alpha that captures tolerance for false positives relative to false negatives, while ensuring that the induced implementation threshold remains interior as events become scarce.

The decision-theoretic analysis therefore yields three central insights. Many classical metrics violate both boundedness and ranking stability, producing thresholds and model rankings that are driven by prevalence rather than discrimination. Rare-event stability is a structural property dictated by a metric’s functional form, not a statistical issue remediable by larger samples or alternative estimators. And in practical environments where rare events carry disproportionate consequences, evaluation metrics must embed cost structures that do not collapse with prevalence. These insights motivate the development of the RES metric family in Section [4](https://arxiv.org/html/2512.00916v1#S4 "4 Rare-Event-Stable Metrics ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts"), where we construct evaluation criteria designed explicitly to retain their interpretability and operational meaning in the rare-event limit.

## 4 Rare-Event-Stable Metrics

Building on the structural failures identified in Section [3](https://arxiv.org/html/2512.00916v1#S3 "3 Decision-Theoretic Foundations ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts"), this section develops a class of performance metrics whose induced decision rules remain coherent as π→0\pi\to 0. A metric is operationally viable in extreme-imbalance settings only if it satisfies the two rare-event requirements of bounded optimal thresholds (Condition C1) and stable model rankings (Condition C2). Metrics meeting these requirements, which we term *rare-event-stable* (RES), maintain interpretability and preserve discrimination even when events are extraordinarily rare. In what follows, we characterise the structural form of such metrics, derive the conditions under which rare-event stability holds, introduce a canonical example, and clarify how these metrics relate to classical measures such as Balanced Accuracy and Youden’s JJ.

Traditional evaluation metrics collapse asymptotically because their marginal penalties for false positives and false negatives diverge as π\pi decreases. When prevalence is small, the negative class dominates expressions involving (1−π)(1-\pi), leading many metrics to overweight the penalty for false positives and forcing the optimal threshold δ∗\delta^{\ast} toward a boundary irrespective of the underlying signal strength. This mechanism explains why measures such as F1, MCC, and accuracy routinely generate degenerate decision rules in rare-event environments. To avoid this outcome, RES metrics must embed a trade-off between the true positive rate (TPR) and the false positive rate (FPR) that does not depend on prevalence. The implied marginal rate comparison must converge to a finite, non-zero limit as π→0\pi\to 0, ensuring that δ∗\delta^{\ast} remains strictly interior. Intuitively, a rare-event-stable metric must reward improvements in extreme-tail detection while penalising false positives in a manner that neither explodes nor collapses with prevalence; metrics whose trade-offs become dominated by the negative class necessarily violate threshold boundedness.

To illustrate this structural requirement, consider metrics that can be expressed or locally approximated in the additive-discriminatory form

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[M​(δ)]=A​(π)​TPR​(δ)−B​(π)​FPR​(δ)+C​(π),A​(π)>0,B​(π)>0.\mathbb{E}[M(\delta)]=A(\pi)\,\mathrm{TPR}(\delta)-B(\pi)\,\mathrm{FPR}(\delta)+C(\pi),\qquad A(\pi)>0,\;B(\pi)>0. |  |

Differentiating with respect to δ\delta yields the first-order condition

|  |  |  |
| --- | --- | --- |
|  | A​(π)​f1​(δ∗)=B​(π)​f0​(δ∗),A(\pi)\,f\_{1}(\delta^{\ast})=B(\pi)\,f\_{0}(\delta^{\ast}), |  |

implying that the optimal threshold satisfies

|  |  |  |
| --- | --- | --- |
|  | f1​(δ∗)f0​(δ∗)=B​(π)A​(π).\frac{f\_{1}(\delta^{\ast})}{f\_{0}(\delta^{\ast})}=\frac{B(\pi)}{A(\pi)}. |  |

When the ratio B​(π)/A​(π)B(\pi)/A(\pi) converges to a finite, positive constant as π→0\pi\to 0, the threshold δ∗​(π)\delta^{\ast}(\pi) converges to an interior limit under the monotone-likelihood-ratio (MLR) assumption, thereby satisfying Condition C1. Conversely, if this ratio diverges or vanishes, the induced threshold collapses to a boundary, rendering the metric operationally meaningless in extreme-imbalance environments.

Metrics that satisfy rare-event stability obey three structural principles. Balanced asymptotics require that the implied trade-off between TPR and FPR remains finite as prevalence declines; no term may diverge like 1/π1/\pi or vanish like π\pi in a manner that distorts the optimisation problem. Tail sensitivity requires that the metric increase when TPR improves at high thresholds, preserving responsiveness to the region of the distribution where rare-event discrimination occurs. Prevalence invariance requires that the effective penalty on false positives not scale implicitly with the size of the negative class; otherwise, the induced threshold necessarily collapses to a boundary. Metrics obeying these principles avoid the degeneracies highlighted in Section [3](https://arxiv.org/html/2512.00916v1#S3 "3 Decision-Theoretic Foundations ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts") and therefore satisfy Conditions C1 and C2. This characterisation offers a practical diagnostic tool, since many classical metrics violate at least one of these principles, explaining their empirical instability in rare-event applications.

A transparent and analytically tractable representative of the RES family is

|  |  |  |  |
| --- | --- | --- | --- |
|  | MRE​(δ)=TPR​(δ)α​FPR​(δ)+(1−α),α∈(0,1).M\_{\mathrm{RE}}(\delta)=\frac{\mathrm{TPR}(\delta)}{\alpha\,\mathrm{FPR}(\delta)+(1-\alpha)},\qquad\alpha\in(0,1). |  | (1) |

This metric possesses three essential properties. First, it is prevalence independent because the denominator contains no prevalence term, ensuring that the marginal trade-off between TPR and FPR remains stable as π\pi decreases. Second, it induces an interior optimal threshold: the maximiser satisfies a likelihood-ratio condition with a finite right-hand side, guaranteeing convergence to a non-degenerate limit and fulfilling Condition C1. Third, its optimisation depends only on the pair (TPR,FPR)(\mathrm{TPR},\mathrm{FPR}), ensuring that model rankings remain consistent across prevalence regimes and satisfying Condition C2. The parameter α\alpha serves as an interpretable policy lever, encoding the institution’s tolerance for false positives relative to false negatives while preserving rare-event stability across the entire preference spectrum. Further discussion of the policy parameter α\alpha, including practical calibration procedures and operational interpretations, is provided in Appendix D.

#### Generalizing the RES Family

While MREM\_{\mathrm{RE}} defined in ([1](https://arxiv.org/html/2512.00916v1#S4.E1 "Equation 1 ‣ 4 Rare-Event-Stable Metrics ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts")) serves as the canonical and most tractable representative, the RES framework encompasses a broader family of functional forms. Any metric M​(δ)M(\delta) can be classified as Rare-Event-Stable provided its marginal rate of substitution between TPR and FPR converges to a finite non-zero constant as π→0\pi\to 0. For example, a generalized family could take the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mgen​(δ)=TPR​(δ)γα​FPR​(δ)+(1−α),γ>0.M\_{\mathrm{gen}}(\delta)=\frac{\mathrm{TPR}(\delta)^{\gamma}}{\alpha\mathrm{FPR}(\delta)+(1-\alpha)},\quad\gamma>0. |  | (2) |

Here, γ\gamma modulates the curvature of the indifference curves in ROC space. We focus on the linear case (γ=1\gamma=1) in this paper because of its direct link to cost-sensitive Bayesian decision theory, but non-linear extensions may offer additional flexibility for institutions with varying risk aversion in the extreme tail.

The structure of MREM\_{\mathrm{RE}} connects naturally to cost-sensitive accuracy. Classical Bayesian decision theory (elkan2001foundations) minimises the loss

|  |  |  |
| --- | --- | --- |
|  | L=π​CF​N​(1−TPR)+(1−π)​CF​P​FPR.L=\pi\,C\_{FN}(1-\mathrm{TPR})+(1-\pi)\,C\_{FP}\,\mathrm{FPR}. |  |

With fixed misclassification costs, the term (1−π)​CF​P​FPR(1-\pi)C\_{FP}\mathrm{FPR} dominates as π→0\pi\to 0, forcing the optimal threshold toward 11 unless costs are explicitly rescaled with prevalence. In many high-stakes settings, however, the cost of missing a rare event increases sharply as the event becomes rarer, effectively scaling as CF​N∝1/πC\_{FN}\propto 1/\pi. Under such conditions, the marginal trade-off embedded in MREM\_{\mathrm{RE}} corresponds precisely to the implicit institutional loss structure, providing a decision-theoretic foundation for the RES formulation and clarifying why prevalence-invariant marginal penalties are essential for coherent alarm rules in extreme-risk environments.

Classical metrics such as Balanced Accuracy and Youden’s JJ satisfy Condition C1 because their optimal thresholds solve the likelihood-ratio equation f1​(δ∗)=f0​(δ∗)f\_{1}(\delta^{\ast})=f\_{0}(\delta^{\ast}), corresponding to an implicit cost ratio of 1:11{:}1. They are therefore technically rare-event-stable. However, they lack tunability, since many institutions require asymmetric weighting of false negatives and false positives that these metrics cannot express. RES metrics such as MREM\_{\mathrm{RE}} generalise these classical measures by introducing a policy parameter while preserving threshold boundedness.

Rare-event-stable metrics offer several advantages in extreme-risk environments. Their induced thresholds reflect stable institutional preferences rather than numerical artefacts of prevalence, ensuring operational alignment across models and samples. Because their marginal trade-offs remain invariant to the size of the negative class, they preserve the meaning of evaluation even under severe imbalance. Their tail sensitivity guarantees that improvements in upper-tail discrimination translate into substantive gains in the evaluation criterion, rather than being dominated by fluctuations in the non-event distribution. Finally, they maintain stable model comparison by avoiding the distortions inherent in metrics whose values are driven primarily by prevalence. These properties make RES metrics suitable for high-stakes applications such as credit-default forecasting, anomaly detection, industrial fault prediction, and systemic-risk surveillance, where traditional metrics routinely fail as events become extremely rare.

Practical procedures for calibrating α\alpha under different institutional settings are presented in Appendix E (Calibration of the Policy Parameter α\alpha).

## 5 Asymptotic Behavior and Robustness Conditions

This section formalizes the asymptotic behaviour of rare-event-stable (RES) metrics as the event probability π\pi approaches zero. Our aim is to characterise the limiting form of the metric-induced optimal threshold, establish conditions under which this threshold remains interior, and contrast these properties with the systematic degeneracies exhibited by widely used performance measures. The analysis connects directly to the coherence requirements introduced in Section [3](https://arxiv.org/html/2512.00916v1#S3 "3 Decision-Theoretic Foundations ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts"), namely bounded optimal thresholds (Condition C1) and stable model rankings (Condition C2).

### 5.1 Preliminaries and Conditional Distribution Structure

Let the conditional forecast distributions be given by

|  |  |  |
| --- | --- | --- |
|  | F1​(t)=Pr⁡(η​(X)≤t∣Y=1),F0​(t)=Pr⁡(η​(X)≤t∣Y=0),F\_{1}(t)=\Pr(\eta(X)\leq t\mid Y=1),\qquad F\_{0}(t)=\Pr(\eta(X)\leq t\mid Y=0), |  |

with associated densities f1​(t)f\_{1}(t) and f0​(t)f\_{0}(t) defined on (0,1)(0,1). The likelihood ratio

|  |  |  |
| --- | --- | --- |
|  | Λ​(t)=f1​(t)f0​(t)\Lambda(t)=\frac{f\_{1}(t)}{f\_{0}(t)} |  |

plays a central role in determining optimal thresholds. Throughout this section we impose a monotone-likelihood-ratio (MLR) condition, which guarantees uniqueness of the induced optimal threshold. Under mild regularity conditions, the functions TPR​(δ)\mathrm{TPR}(\delta) and FPR​(δ)\mathrm{FPR}(\delta) are continuously differentiable in δ\delta, permitting the use of standard first-order optimality arguments.

### 5.2 Limiting Form of the Optimal Threshold for RES Metrics

Consider a RES metric whose expected value can be represented as

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[M​(δ)]=A​(π)​TPR​(δ)−B​(π)​FPR​(δ)+C​(π),\mathbb{E}[M(\delta)]=A(\pi)\,\mathrm{TPR}(\delta)-B(\pi)\,\mathrm{FPR}(\delta)+C(\pi), |  |

with A​(π)>0A(\pi)>0 and B​(π)>0B(\pi)>0. Differentiating with respect to δ\delta yields the first-order condition

|  |  |  |
| --- | --- | --- |
|  | A​(π)​f1​(δ∗)=B​(π)​f0​(δ∗),A(\pi)\,f\_{1}(\delta^{\ast})=B(\pi)\,f\_{0}(\delta^{\ast}), |  |

so that the optimal threshold satisfies the likelihood-ratio equation

|  |  |  |
| --- | --- | --- |
|  | Λ​(δ∗)=B​(π)A​(π).\Lambda(\delta^{\ast})=\frac{B(\pi)}{A(\pi)}. |  |

A metric is rare-event-stable if and only if the marginal penalty ratio converges to a finite, positive limit:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0<limπ→0B​(π)A​(π)<∞.0<\lim\_{\pi\to 0}\frac{B(\pi)}{A(\pi)}<\infty. |  | (3) |

Under the MLR condition, the induced threshold therefore converges to a unique interior point δ∞\delta\_{\infty} that solves

|  |  |  |
| --- | --- | --- |
|  | Λ​(δ∞)=limπ→0B​(π)A​(π).\Lambda(\delta\_{\infty})=\lim\_{\pi\to 0}\frac{B(\pi)}{A(\pi)}. |  |

This captures the bounded-threshold requirement (Condition C1) and shows that RES metrics maintain coherent decision rules even when π\pi becomes arbitrarily small.

### 5.3 Robustness to Reductions in Event Probability

Metrics satisfying ([3](https://arxiv.org/html/2512.00916v1#S5.E3 "Equation 3 ‣ 5.2 Limiting Form of the Optimal Threshold for RES Metrics ‣ 5 Asymptotic Behavior and Robustness Conditions ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts")) possess several forms of robustness as prevalence declines. First, threshold continuity holds: if the ratio B​(π)/A​(π)B(\pi)/A(\pi) varies smoothly in π\pi, then the induced threshold δ∗​(π)\delta^{\ast}(\pi) varies smoothly as well, ensuring predictable behaviour under changing imbalance conditions, specifically prior probability shift (moreno2012unifying). Second, preservation of model ordering is guaranteed: if model A dominates model B in likelihood-ratio ordering, then MA​(π)M\_{A}(\pi) exceeds MB​(π)M\_{B}(\pi) for all sufficiently small π\pi, thereby satisfying Condition C2. Third, RES metrics exhibit resilience in finite samples, since their dependence on the pair (TPR,FPR)(\mathrm{TPR},\mathrm{FPR}) rather than on raw event counts enables stable behaviour even when the number of observed positive cases is extremely small.

#### Relaxation of the MLR Assumption

The asymptotic analysis relies on the Monotone Likelihood Ratio (MLR) property to guarantee the uniqueness of the optimal threshold δ∗\delta^{\ast}. In practice, highly complex models such as deep neural networks may produce calibrated probabilities that do not strictly satisfy MLR, potentially resulting in a likelihood ratio Λ​(δ)\Lambda(\delta) that is non-monotonic. It is important to note that the rare-event stability of RES metrics does not depend on uniqueness. Even if Λ​(δ)\Lambda(\delta) oscillates, the condition for stability (Equation [3](https://arxiv.org/html/2512.00916v1#S5.E3 "Equation 3 ‣ 5.2 Limiting Form of the Optimal Threshold for RES Metrics ‣ 5 Asymptotic Behavior and Robustness Conditions ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts")) ensures that *all* local maxima of the RES metric remain strictly interior as π→0\pi\to 0. In contrast, traditional metrics such as the F1-score suffer from structural collapse where the optimality condition diverges to the boundary regardless of the shape of Λ​(δ)\Lambda(\delta). Therefore, while MLR violation may introduce local optima, it does not compromise the fundamental resistance of RES metrics to prevalence-driven threshold collapse.

### 5.4 Why Standard Metrics Fail Asymptotically

The asymptotic framework also clarifies the structural failures of widely used metrics. Precision–recall measures such as F1 and FβF\_{\beta} rely on

|  |  |  |
| --- | --- | --- |
|  | Prec​(δ)=π​TPR​(δ)π​TPR​(δ)+(1−π)​FPR​(δ),\mathrm{Prec}(\delta)=\frac{\pi\,\mathrm{TPR}(\delta)}{\pi\,\mathrm{TPR}(\delta)+(1-\pi)\,\mathrm{FPR}(\delta)}, |  |

and as π→0\pi\to 0, the denominator becomes dominated by (1−π)​FPR​(δ)(1-\pi)\,\mathrm{FPR}(\delta), causing precision to collapse unless FPR​(δ)\mathrm{FPR}(\delta) shrinks at an extreme rate. Maximising F1 therefore drives δ∗\delta^{\ast} toward zero to inflate recall or toward one to inflate precision, depending on the tail shape of the score distribution. This instability reflects the fact that F1 induces a prevalence-dependent implicit cost ratio, a structural incoherence formally derived by hand2018note. Either outcome violates Conditions C1 and C2. Correlation-based metrics such as MCC contain multiplicative π​(1−π)\sqrt{\pi(1-\pi)} factors that direct optimisation toward δ∗→1\delta^{\ast}\to 1, effectively producing a never-alarm rule even for strongly discriminative models and thereby violating threshold boundedness. Accuracy and fixed-cost variants suffer an analogous failure: since Acc=π​TPR+(1−π)​TNR\mathrm{Acc}=\pi\,\mathrm{TPR}+(1-\pi)\,\mathrm{TNR}, accuracy converges to TNR\mathrm{TNR} as π→0\pi\to 0 and thus ignores upper-tail discrimination altogether, violating ranking stability. Although AUC does not involve an explicit threshold and therefore does not violate Condition C1, ROC geometry becomes dominated by the negative class as prevalence decreases. AUC saturates near unity even when models differ substantially in tail behaviour, violating Condition C2 and rendering the metric uninformative in rare-event environments. These failures are structural, arising from the divergence or vanishing of B​(π)/A​(π)B(\pi)/A(\pi), and not merely consequences of sampling variability.

### 5.5 Practical Implications

The asymptotic analysis yields several practical implications for evaluation under extreme rarity. RES metrics induce stable thresholds that remain coherent even when the event probability is extremely small, ensuring operational interpretability. They support consistent model comparison by maintaining meaningful performance rankings across prevalence regimes and avoiding the distortions that plague classical measures. They offer robustness under data scarcity because they depend on the shape of the forecast distribution in the extreme upper tail rather than on the absolute number of observed events. Finally, they provide tail-sensitive evaluation: improvements in the region of the distribution most relevant for detecting rare events translate directly into metric gains, aligning evaluation with institutional priorities. These asymptotic properties underpin the empirical findings in Sections [6](https://arxiv.org/html/2512.00916v1#S6 "6 Simulation Design and Results ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts") and [7](https://arxiv.org/html/2512.00916v1#S7 "7 Application: Credit-Default Forecasting Under Extreme Rarity ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts"), where RES metrics consistently display stability and interpretability in sharp contrast to the collapse exhibited by traditional measures. Additional robustness checks and supplementary asymptotic diagnostics appear in Appendices B and E.

## 6 Simulation Design and Results

The simulation study evaluates the behaviour of rare-event-stable (RES) metrics under controlled conditions spanning five orders of magnitude in prevalence. We consider two signal regimes defined by the degree of distributional overlap between classes: a *Moderate* regime (implied AUC≈0.90\mathrm{AUC}\approx 0.90), representing standard credit-scoring performance, and a *Strong* regime (implied AUC>0.99\mathrm{AUC}>0.99), representing near-ideal separation often seen in distinct failure-mode detection. The data-generating processes and metric calculation procedures are detailed in Appendix B. Here we report the main results, focusing on threshold drift, discriminative resolution, and the stability properties of RES metrics.

Detailed descriptions of the simulation design, including sampling procedures, parameter settings, and implementation details, are provided in Appendix C.

Prevalence is varied exogenously. For each target value π∈{10−2,10−3,10−4,10−5,10−6}\pi\in\{10^{-2},10^{-3},10^{-4},10^{-5},10^{-6}\}, stratified samples are constructed by fixing the number of positive observations and choosing the number of negatives implied by the selected prevalence. At the most extreme rarity level, such as π=10−6\pi=10^{-6}, this procedure yields samples containing, for example, 2020 positive and 2020 million negative observations, capturing the geometry of the rare-event limit without introducing additional resampling noise. Across all regimes, 2,0002{,}000 independent replications are generated. For every metric, discrimination regime, and prevalence level, the optimal threshold δ∗\delta^{\ast} is computed exactly by tracing the full confusion-matrix path. This design enables a direct examination of whether traditional metrics undergo threshold instability as π→0\pi\to 0, whether RES metrics maintain stable interior thresholds, and whether discrimination-based ranking is preserved as prevalence varies.

### 6.1 Instability of Classical Metrics

Traditional measures exhibit substantial and systematic deterioration as prevalence declines. Table [1](https://arxiv.org/html/2512.00916v1#S6.T1 "Table 1 ‣ 6.1 Instability of Classical Metrics ‣ 6 Simulation Design and Results ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts") summarises the range of optimal thresholds for the F1-score, Balanced Accuracy (BA), the Matthews Correlation Coefficient (MCC), and AUC across five orders of magnitude in π\pi. Even in this fully controlled experimental setting, large shifts in δ∗\delta^{\ast} appear, indicating that threshold instability is a structural property of these metrics rather than an artefact of sampling variation.

Table 1: Optimal threshold ranges for traditional metrics across five prevalence levels (10−210^{-2} to 10−610^{-6}).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Model | F1 Range | BA Range | MCC Range | AUC Range |
| Moderate | 0.552 – 0.992 | 0.242 – 0.599 | 0.532 – 0.992 | 0.879 – 0.999 |
| Strong | 0.426 – 0.842 | 0.223 – 0.776 | 0.426 – 0.842 | 0.996 – 1.000 |

The F1-score displays pronounced threshold drift: in the Moderate regime, the optimal threshold moves from interior values (around 0.550.55) toward the upper boundary (around 0.990.99) as prevalence declines. While MCC is frequently recommended as a reliable, informative alternative to F1 in imbalanced settings (chicco2020advantages), our results indicate that this robustness does not extend to the rare-event limit. MCC exhibits a nearly identical migration to F1, with its optimal threshold spanning 0.530.53–0.990.99 in the Moderate regime and 0.430.43–0.840.84 in the Strong regime. Balanced Accuracy also shows substantial movement, with shifts exceeding 0.550.55 under Strong separation. These changes are operationally significant: a classifier calibrated for a moderately imbalanced environment would adopt nearly opposite intervention rules under extreme rarity. The monotonic nature of this migration is illustrated in Figure [1](https://arxiv.org/html/2512.00916v1#S6.F1 "Figure 1 ‣ 6.1 Instability of Classical Metrics ‣ 6 Simulation Design and Results ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts")(left).

Table [2](https://arxiv.org/html/2512.00916v1#S6.T2 "Table 2 ‣ 6.1 Instability of Classical Metrics ‣ 6 Simulation Design and Results ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts") reports the statistical significance of the relationship between the optimal threshold δ∗\delta^{\ast} (or the AUC value) and log10⁡(π)\log\_{10}(\pi). All correlations are highly significant (p<0.001p<0.001), confirming that the observed instability arises from the underlying metric structure rather than simulation noise.

Table 2: Significance tests for metric instability (Spearman correlation with log10⁡(π)\log\_{10}(\pi)).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Model | F1 (pp) | BA (pp) | MCC (pp) | AUC (pp) |
| Moderate | <0.001<0.001 | <0.001<0.001 | <0.001<0.001 | <0.001<0.001 |
| Strong | <0.001<0.001 | <0.001<0.001 | <0.001<0.001 | <0.001<0.001 |

Although AUC does not induce a decision threshold directly, its behaviour illustrates the loss of discriminative resolution in the extreme tail. In the Strong regime, the AUC range is 0.9960.996–1.0001.000 (Table [1](https://arxiv.org/html/2512.00916v1#S6.T1 "Table 1 ‣ 6.1 Instability of Classical Metrics ‣ 6 Simulation Design and Results ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts")). While AUC remains a robust metric for global ranking across the entire distribution, this saturation effect renders it uninformative for distinguishing between models specifically in the rare-event limit (Figure [1](https://arxiv.org/html/2512.00916v1#S6.F1 "Figure 1 ‣ 6.1 Instability of Classical Metrics ‣ 6 Simulation Design and Results ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts"), right). The combined evidence confirms that standard metrics either collapse to boundary thresholds or lose discriminative power as π→0\pi\to 0, matching the structural failures predicted by the analytical results.

![Refer to caption](x1.png)

![Refer to caption](x2.png)

Figure 1: Behaviour of traditional metrics under extreme rarity. Left: F1-score thresholds increase monotonically as prevalence decreases (p<0.001p<0.001). Right: AUC saturates near 1.01.0, losing discriminatory power in the extreme tail.

### 6.2 Stability of RES Metrics

The RES metrics behave in a manner fully aligned with theoretical expectations. Their induced thresholds remain interior across all prevalence levels, vary smoothly as π\pi changes, and maintain a clear distinction between the Moderate and Strong discrimination regimes. Table [3](https://arxiv.org/html/2512.00916v1#S6.T3 "Table 3 ‣ 6.2 Stability of RES Metrics ‣ 6 Simulation Design and Results ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts") reports mean thresholds and coefficients of variation across the full range of π\pi.

Table 3: Stability of RES metric thresholds across five prevalence levels.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Model | α\alpha | Mean δ∗\delta^{\ast} | MRE CV | Threshold CV |
| Moderate | 0.10 | 0.289 | 0.014 | 0.213 |
| Moderate | 0.25 | 0.335 | 0.026 | 0.151 |
| Moderate | 0.50 | 0.391 | 0.041 | 0.108 |
| Strong | 0.10 | 0.471 | 0.001 | 0.193 |
| Strong | 0.25 | 0.472 | 0.001 | 0.189 |
| Strong | 0.50 | 0.476 | 0.003 | 0.178 |

RES thresholds exhibit strong prevalence invariance. In the Strong regime with α=0.50\alpha=0.50, the mean threshold is approximately 0.4760.476 across six orders of magnitude in prevalence. The coefficients of variation are far below those observed for classical metrics, indicating that RES thresholds remain stable and do not drift toward boundary behaviour as π\pi declines. This stability reflects the prevalence-invariant marginal trade-off embedded in the RES formulation.

The parameter α\alpha consistently encodes institutional risk preferences. Lower values generate conservative thresholds with fewer alarms, whereas higher values increase sensitivity. Importantly, these relationships persist across all levels of prevalence, demonstrating that RES metrics transmit policy preferences coherently even in extreme rarity.

![Refer to caption](x3.png)


Figure 2: Stability of RES thresholds. Optimal thresholds remain interior and nearly constant across all prevalence levels. The parameter α\alpha modulates preferences while preserving threshold stability.

Overall, the RES metrics satisfy both threshold boundedness and ranking stability. Their simulated behaviour mirrors the analytical characterisation developed in earlier sections and contrasts sharply with the structural collapse observed for traditional measures.

### 6.3 Summary of Simulation Findings

The simulation results reveal a clear and systematic distinction between the behaviour
of traditional performance metrics and that of the proposed RES metrics under rare-event
scaling. Classical measures such as the F1-score, Balanced Accuracy, and MCC exhibit
substantial threshold drift as π\pi decreases, with optimal thresholds migrating
towards boundary values and, in many cases, converging to near-degenerate operating
regions. Their behaviour is monotone, statistically significant across all regimes, and
consistent with the structural collapse predicted by the theoretical analysis.

AUC behaves differently but suffers an analogous pathology: as prevalence declines,
its value saturates near one, eliminating meaningful discriminative resolution in the
extreme tail. This saturation violates ranking stability, causing models with materially
different tail geometry to appear indistinguishable when evaluated by AUC.

In contrast, RES metrics maintain interior, stable, and prevalence-invariant optimal
thresholds. Across five orders of magnitude in π\pi, RES thresholds exhibit limited
dispersion, smooth adjustment across regimes, and negligible variability in metric
values. The parameter α\alpha consistently encodes institutional preferences without
interacting with prevalence, demonstrating that the RES framework preserves both the
interpretation and the operational meaning of model evaluation in rare-event settings.

Overall, the simulation evidence confirms that classical metrics undergo structural
instability as π→0\pi\to 0, whereas RES metrics satisfy both threshold boundedness and
ranking stability. These properties establish RES metrics as reliable evaluation tools
in extreme imbalance environments and motivate their use in the empirical application
that follows.

Extended tables and supplementary simulation diagnostics appear in Appendix G; full empirical tables: Appendix F.

## 7 Application: Credit-Default Forecasting Under Extreme Rarity

This section evaluates the empirical performance of the RES metrics in a real forecasting environment using the “Give Me Some Credit” dataset from Kaggle, a widely used consumer-credit panel containing borrower characteristics and a binary indicator of serious delinquency within two years. The empirical design follows standard practice in the forecast-evaluation literature. The dataset and forecasting model are described, controlled prevalence regimes are constructed to emulate increasing rarity, and the behaviour of threshold-based metrics is analysed across these regimes. The results demonstrate that the structural instabilities identified in the theoretical and simulation analyses
manifest clearly in real data, whereas the RES framework maintains stability and interpretability throughout.

### 7.1 Data and Model Specification

The dataset includes borrower-level financial and demographic variables alongside a binary default indicator. After standard preprocessing and median imputation, a LightGBM model is trained on a stratified 70% subsample, with the remaining 30% held out for evaluation. The model produces calibrated probability-of-default forecasts p^i\widehat{p}\_{i}, which remain fixed across all experiments so that variation in metric behaviour reflects solely the evaluation criteria rather than changes in model specification. Further descriptive statistics and preprocessing details appear in Appendix D (Application: Data & Model).

The natural prevalence of default in the test sample is 6.64%. To assess threshold behaviour under increasing rarity, additional evaluation regimes are created by down-sampling positive observations while retaining all negatives. This design preserves the geometry of low-prevalence environments without introducing artificial resampling artefacts, mirroring the ‘Low Default Portfolio’ (LDP) problem common in regulatory risk modelling (pluto2011estimating). Table [F.2](https://arxiv.org/html/2512.00916v1#A6.T2 "Table F.2 ‣ F.2 Prevalence Regimes ‣ F Empirical Calibration and Results ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts") summarises the resulting sample sizes.

Table 4: Construction of prevalence regimes used in the empirical analysis.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Target π\pi | Empirical π\pi | NN | Positives | Negatives |
| 0.0010 | 0.0010 | 42056 | 42 | 42014 |
| 0.0050 | 0.0050 | 42225 | 211 | 42014 |
| 0.0100 | 0.0100 | 42438 | 424 | 42014 |
| 0.0200 | 0.0200 | 42871 | 857 | 42014 |
| 0.0664 | 0.0664 | 45000 | 2986 | 42014 |

### 7.2 Bootstrap Design

Within each prevalence regime, 500500 bootstrap samples of fixed size are drawn
(efron1993bootstrap). For each replication, the predicted probabilities are sorted in descending order to trace the full confusion-matrix path as a function of the threshold δ\delta. This procedure yields the exact threshold δ∗\delta^{\ast} that maximises each metric in each bootstrap replication. Repeating this process across samples produces empirical distributions of optimal thresholds and metric values, enabling a clean distinction between structural behaviour and sampling variability.
Summary statistics for these distributions appear in Tables [F.3](https://arxiv.org/html/2512.00916v1#A6.T3 "Table F.3 ‣ F.3 Stability Analysis Tables ‣ F Empirical Calibration and Results ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts")–[F.4](https://arxiv.org/html/2512.00916v1#A6.T4 "Table F.4 ‣ F.3 Stability Analysis Tables ‣ F Empirical Calibration and Results ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts").

### 7.3 Threshold Behaviour of Classical Metrics

Traditional metrics exhibit substantial and systematic threshold drift as prevalence declines. Figure [3](https://arxiv.org/html/2512.00916v1#S7.F3 "Figure 3 ‣ 7.3 Threshold Behaviour of Classical Metrics ‣ 7 Application: Credit-Default Forecasting Under Extreme Rarity ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts") shows that the optimal thresholds for F1, MCC, and Balanced Accuracy increase monotonically with rarity, with especially large movements in the rarest regime (π=0.001\pi=0.001). This pattern is fully consistent with the threshold-collapse mechanism predicted by the theoretical framework.

![Refer to caption](x4.png)


Figure 3: Optimal thresholds δ∗\delta^{\ast} for F1, MCC, and Balanced Accuracy across
prevalence regimes. Thresholds drift sharply upward as prevalence declines,
revealing structural instability.

Table [F.3](https://arxiv.org/html/2512.00916v1#A6.T3 "Table F.3 ‣ F.3 Stability Analysis Tables ‣ F Empirical Calibration and Results ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts") quantifies this instability. F1 and MCC exhibit threshold ranges exceeding 0.55 and 0.64 respectively, with coefficients of variation between 0.34 and 0.40. These imply large and economically significant shifts in the alarm policy across regimes. Balanced Accuracy is numerically stable but effectively rigid, consistently selecting a threshold between 2% and 19%, which limits its relevance when false positives and false negatives carry asymmetric costs.

Table 5: Threshold stability of traditional metrics across prevalence regimes.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Metric | Min δ∗\delta^{\ast} | Max δ∗\delta^{\ast} | Range | CV |
| Balanced Accuracy | 0.02 | 0.19 | 0.17 | 0.26 |
| F1–Score | 0.16 | 0.71 | 0.55 | 0.34 |
| MCC | 0.07 | 0.71 | 0.64 | 0.40 |

Instability is also evident within each prevalence level. Figure [4](https://arxiv.org/html/2512.00916v1#S7.F4 "Figure 4 ‣ 7.3 Threshold Behaviour of Classical Metrics ‣ 7 Application: Credit-Default Forecasting Under Extreme Rarity ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts") shows that both F1 and MCC exhibit substantial within-regime dispersion, indicating limited guidance regarding a stable implementation threshold even when the underlying forecast distribution is unchanged.

![Refer to caption](x5.png)


Figure 4: Coefficient of variation of optimal thresholds within each prevalence
regime. Classical metrics exhibit significant within-regime volatility.

At π≈0.001\pi\approx 0.001, the volatility becomes extreme. Figure [5](https://arxiv.org/html/2512.00916v1#S7.F5 "Figure 5 ‣ 7.3 Threshold Behaviour of Classical Metrics ‣ 7 Application: Credit-Default Forecasting Under Extreme Rarity ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts") shows the bootstrap distribution of F1-optimal thresholds, revealing wide dispersion and many replications exceeding 0.70—an operationally implausible pattern for credit-risk screening.

![Refer to caption](x6.png)


Figure 5: Distribution of F1-optimal thresholds at π≈0.001\pi\approx 0.001. The wide dispersion illustrates pronounced instability in extremely rare-event settings.

### 7.4 Stability of RES Metrics

The RES metrics exhibit fundamentally different behaviour. As shown in
Figure [6](https://arxiv.org/html/2512.00916v1#S7.F6 "Figure 6 ‣ 7.4 Stability of RES Metrics ‣ 7 Application: Credit-Default Forecasting Under Extreme Rarity ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts"), their optimal thresholds remain interior and stable across all prevalence levels. Thresholds adjust smoothly with α\alpha and preserve their relative ordering across regimes, reflecting consistent transmission of institutional preferences.

![Refer to caption](x7.png)


Figure 6: Optimal RES thresholds δ∗\delta^{\ast} for α∈{0.10,0.25,0.50}\alpha\in\{0.10,0.25,0.50\}.
Thresholds remain interior and stable even under extreme rarity.

Table [F.4](https://arxiv.org/html/2512.00916v1#A6.T4 "Table F.4 ‣ F.3 Stability Analysis Tables ‣ F Empirical Calibration and Results ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts") summarises these results. Across the full range of α∈{0.10,0.25,0.50}\alpha\in\{0.10,0.25,0.50\}, mean RES-threshold values remain strictly interior, lying between 1% and 4%. Although the coefficient of variation is higher for α=0.10\alpha=0.10 (CV = 0.52) due to increased sensitivity in the extreme tail, the absolute location of the thresholds still defines economically interpretable operating regions across all prevalence levels. This behaviour stands in sharp contrast to the boundary collapse observed for classical metrics.

Table 6: RES metric performance across prevalence regimes.

|  |  |  |  |
| --- | --- | --- | --- |
| α\alpha | Mean δ∗\delta^{\ast} | Threshold CV | MRE CV |
| 0.10 | 0.01 | 0.52 | 0.01 |
| 0.25 | 0.02 | 0.38 | 0.02 |
| 0.50 | 0.04 | 0.35 | 0.05 |

### 7.5 Operational Implications

Table [7](https://arxiv.org/html/2512.00916v1#S7.T7 "Table 7 ‣ 7.5 Operational Implications ‣ 7 Application: Credit-Default Forecasting Under Extreme Rarity ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts") aggregates the empirical stability results into operational
categories. F1 and MCC require large, prevalence-driven adjustments in δ∗\delta^{\ast}, leading to unstable and difficult-to-defend alarm rules. Balanced Accuracy is stable but rigid and suitable only for symmetric-cost environments. RES metrics exhibit both stability and flexibility, allowing α\alpha to encode institutional preferences while preserving stable operating points.

Table 7: Operational implications of threshold behaviour across metrics.

|  |  |  |  |
| --- | --- | --- | --- |
| Metric | Range | CV | Recommendation |
| Balanced Accuracy | 0.174 | 0.26 | Symmetric Only |
| F1–Score | 0.547 | 0.34 | Avoid (High Drift) |
| MCC | 0.641 | 0.40 | Avoid (High Drift) |
| RES (α=0.10\alpha=0.10) | 0.031 | 0.52 | Recommended (Stable) |
| RES (α=0.25\alpha=0.25) | 0.077 | 0.38 | Recommended (Stable) |
| RES (α=0.50\alpha=0.50) | 0.157 | 0.35 | Recommended (Stable) |

The link between institutional constraints and α\alpha is shown in
Table [F.1](https://arxiv.org/html/2512.00916v1#A6.T1 "Table F.1 ‣ F.1 Calibrated Values ‣ F Empirical Calibration and Results ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts"). A historical 5% alarm-rate rule corresponds to
α^A=0.56\widehat{\alpha}\_{A}=0.56. A 3% capacity constraint corresponds to
α^B=0.99\widehat{\alpha}\_{B}=0.99. A loss-based calibration with cost ratio (1:20)(1{:}20) yields α^C=0.05\widehat{\alpha}\_{C}=0.05 and an induced threshold of approximately 1%. These values span the full range of operational postures—from highly conservative to highly sensitive-and demonstrate the transparency with which RES metrics encode policy
preferences.

Table 8: Calibrated values of the policy parameter α\alpha under three operational
scenarios.

|  |  |  |
| --- | --- | --- |
| Scenario | Calibrated α\alpha | Induced Threshold |
| A: Historical (5%) | 0.56 | 0.05 |
| B: Capacity (3%) | 0.99 | 0.46 |
| C: Loss (1:20) | 0.05 | 0.01 |

### 7.6 Summary

The empirical evidence shows that classical metrics are structurally unstable in rare-event credit-default forecasting. Their optimal thresholds drift sharply across prevalence regimes and exhibit substantial volatility within regimes, often yielding operationally implausible alarm rules. RES metrics behave fundamentally differently:
they maintain interior, stable, and economically interpretable thresholds even under extreme rarity. The calibrated values of α\alpha illustrate how the RES framework separates stable institutional preferences from the data-driven implementation threshold δ∗\delta^{\ast}, enabling consistent decision criteria across models, sampling regimes, and prevalence environments. These results corroborate the theoretical and simulation findings and underline the practical relevance of the RES framework for real-world extreme-risk forecasting applications.

Supplementary figures, threshold distributions, and additional diagnostics appear in Appendices G–H (Simulation & Application diagnostics; full tables in Appendix F).

## 8 Conclusion

This paper introduced a class of Rare-Event-Stable (RES) performance metrics designed for binary classification in environments where events occur with extremely low prevalence. We showed, both analytically and empirically, that widely used threshold-dependent metrics such as the F1-score, the Matthews Correlation Coefficient, and Balanced Accuracy possess inherent structural weaknesses in such settings. As the event probability declines, their induced decision thresholds drift systematically across prevalence regimes and exhibit substantial dispersion within fixed regimes, resulting in intervention policies that are operationally inconsistent and difficult to justify.

The RES framework resolves this instability by introducing a policy parameter α\alpha that captures an institution’s relative tolerance for false positives and false negatives. A central feature of the approach is the clear separation between the stable preference parameter α\alpha and the data-driven implementation threshold δ∗\delta^{\ast}. While δ∗\delta^{\ast} responds to the empirical score distribution, the institutional preference encoded by α\alpha remains invariant across models, samples, and operational environments. This distinction provides a coherent foundation for decision-making in *extreme-imbalance environments*, ensuring that institutional priorities are preserved even as empirical conditions vary.

The theoretical properties of the RES metrics were validated through extensive simulation experiments spanning five orders of magnitude in prevalence. Classical metrics exhibited the predicted threshold collapse, while RES metrics maintained interior, stable, and economically interpretable decision boundaries throughout. An empirical application using consumer credit-default data reinforced these findings. The RES framework facilitated transparent calibration of α\alpha to several operational targets, including historical policy thresholds, institutional capacity constraints, and explicit loss structures. The resulting calibrated values demonstrated how diverse institutional postures are naturally encoded within the RES metric family.

While the RES framework focuses on decision thresholds, it is not intended to replace proper scoring rules such as the Brier score or the logarithmic score. Proper scoring rules evaluate the calibration and refinement of the entire predictive distribution, providing a necessary foundation for probabilistic forecasting. However, they do not directly guide the binary interventions required in operational settings. We view these approaches as complementary: proper scoring rules should be used to select and calibrate models during development, while RES metrics provide the stability and interpretability required to set operational alarm thresholds in the tail. A holistic evaluation framework for extreme risks should therefore pair a tail-weighted proper scoring rule (for distributional assessment) with an RES metric (for decision-policy definition).

Future research may extend these ideas to multiclass and multilabel settings, where dependence structures among rare event classes introduce additional challenges. Another promising direction involves reconciling the RES framework with proper scoring rules (gneiting2011comparing). While RES provides decision-theoretic stability in the extreme tail, proper scoring rules evaluate global probabilistic calibration. Developing a principled way to bridge these complementary objectives remains an open problem in extreme-risk forecasting.

Appendices

## A Formal Asymptotic Derivations

This appendix provides the mathematical proofs supporting the structural claims made in Section 5 of the main text regarding the stability of RES metrics and the asymptotic collapse of the F1-score.

### A.1 Optimality Condition for RES Metrics

Recall the definition of the Rare-Event-Stable metric:

|  |  |  |  |
| --- | --- | --- | --- |
|  | MRE​(δ;α)=TPR​(δ)α​FPR​(δ)+(1−α).M\_{\mathrm{RE}}(\delta;\alpha)=\frac{\mathrm{TPR}(\delta)}{\alpha\,\mathrm{FPR}(\delta)+(1-\alpha)}. |  | (4) |

To find the optimal threshold δ∗\delta^{\ast}, we differentiate MREM\_{\mathrm{RE}} with respect to the decision threshold δ\delta and set the derivative to zero. Let f1​(δ)f\_{1}(\delta) and f0​(δ)f\_{0}(\delta) denote the conditional densities of the score for positive and negative cases, respectively. The derivatives of the rates with respect to the threshold are given by ∂TPR∂δ=−f1​(δ)\frac{\partial\mathrm{TPR}}{\partial\delta}=-f\_{1}(\delta) and ∂FPR∂δ=−f0​(δ)\frac{\partial\mathrm{FPR}}{\partial\delta}=-f\_{0}(\delta).

Applying the quotient rule for differentiation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂MRE∂δ=−f1​(δ)​[α​FPR​(δ)+(1−α)]−TPR​(δ)​[−α​f0​(δ)][α​FPR​(δ)+(1−α)]2=0.\frac{\partial M\_{\mathrm{RE}}}{\partial\delta}=\frac{-f\_{1}(\delta)[\alpha\,\mathrm{FPR}(\delta)+(1-\alpha)]-\mathrm{TPR}(\delta)[-\alpha f\_{0}(\delta)]}{[\alpha\,\mathrm{FPR}(\delta)+(1-\alpha)]^{2}}=0. |  | (5) |

For the numerator to be zero, the following equality must hold:

|  |  |  |
| --- | --- | --- |
|  | f1​(δ)​[α​FPR​(δ)+(1−α)]=α​TPR​(δ)​f0​(δ).f\_{1}(\delta)[\alpha\,\mathrm{FPR}(\delta)+(1-\alpha)]=\alpha\,\mathrm{TPR}(\delta)f\_{0}(\delta). |  |

Rearranging terms to isolate the likelihood ratio Λ​(δ)=f1​(δ)/f0​(δ)\Lambda(\delta)=f\_{1}(\delta)/f\_{0}(\delta), we obtain the first-order condition (FOC):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ​(δ∗)=α​TPR​(δ∗)α​FPR​(δ∗)+(1−α).\Lambda(\delta^{\ast})=\frac{\alpha\,\mathrm{TPR}(\delta^{\ast})}{\alpha\,\mathrm{FPR}(\delta^{\ast})+(1-\alpha)}. |  | (6) |

Result: The right-hand side of ([6](https://arxiv.org/html/2512.00916v1#A1.E6 "Equation 6 ‣ A.1 Optimality Condition for RES Metrics ‣ A Formal Asymptotic Derivations ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts")) contains no prevalence term π\pi. It depends solely on the shape of the ROC curve (via TPR and FPR) and the policy preference parameter α\alpha. Consequently, as π→0\pi\to 0, the condition defining δ∗\delta^{\ast} remains mathematically invariant, ensuring the structural stability of the decision threshold.

### A.2 Asymptotic Collapse of the F1-Score

The F1-score is defined as the harmonic mean of Precision and Recall. Expressed in terms of rates and prevalence π\pi:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​1​(δ)=2​π​TPR​(δ)2​π​TPR​(δ)+(1−π)​FPR​(δ).F1(\delta)=\frac{2\pi\,\mathrm{TPR}(\delta)}{2\pi\,\mathrm{TPR}(\delta)+(1-\pi)\,\mathrm{FPR}(\delta)}. |  | (7) |

Maximizing F​1F1 is equivalent to maximizing its natural logarithm. Differentiating ln⁡(F​1)\ln(F1) with respect to δ\delta yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂ln⁡F​1∂δ=−f1​(δ)TPR​(δ)−−2​π​f1​(δ)−(1−π)​f0​(δ)2​π​TPR​(δ)+(1−π)​FPR​(δ)=0.\frac{\partial\ln F1}{\partial\delta}=\frac{-f\_{1}(\delta)}{\mathrm{TPR}(\delta)}-\frac{-2\pi f\_{1}(\delta)-(1-\pi)f\_{0}(\delta)}{2\pi\,\mathrm{TPR}(\delta)+(1-\pi)\,\mathrm{FPR}(\delta)}=0. |  | (8) |

Rearranging to solve for the likelihood ratio Λ​(δ∗)=f1​(δ∗)/f0​(δ∗)\Lambda(\delta^{\ast})=f\_{1}(\delta^{\ast})/f\_{0}(\delta^{\ast}) yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ​(δ∗)=(1−π2​π)⋅TPR​(δ∗)2​π​TPR​(δ∗)+(1−π)​FPR​(δ∗).\Lambda(\delta^{\ast})=\left(\frac{1-\pi}{2\pi}\right)\cdot\frac{\mathrm{TPR}(\delta^{\ast})}{2\pi\,\mathrm{TPR}(\delta^{\ast})+(1-\pi)\,\mathrm{FPR}(\delta^{\ast})}. |  | (9) |

Result: Consider the limit as π→0\pi\to 0. The leading term 1−π2​π\frac{1-\pi}{2\pi} diverges to infinity. Unless the second fraction vanishes at a commensurate rate (which implies TPR→0\mathrm{TPR}\to 0), the required likelihood ratio must diverge. For standard unimodal score distributions, a diverging likelihood ratio requirement forces the optimal threshold δ∗→1\delta^{\ast}\to 1.

![Refer to caption](x8.png)


Figure A.1: Geometric mechanism of threshold collapse. The optimal threshold δ∗\delta^{\ast} is determined by the intersection of the model likelihood ratio and the metric’s marginal trade-off curve. The RES curve depends only on α\alpha and stays fixed, yielding a stable interior intersection consistent with [Equation˜6](https://arxiv.org/html/2512.00916v1#A1.E6 "In A.1 Optimality Condition for RES Metrics ‣ A Formal Asymptotic Derivations ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts"). In contrast, the F1F\_{1} curves diverge upward with decreasing prevalence (10−2→10−310^{-2}\to 10^{-3}), pushing δ∗→1\delta^{\ast}\to 1 as implied by [Equation˜9](https://arxiv.org/html/2512.00916v1#A1.E9 "In A.2 Asymptotic Collapse of the F1-Score ‣ A Formal Asymptotic Derivations ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts"). Note the logarithmic scale on the y-axis.

## B Computational Strategy for Extreme Rarity

Simulating rare events at prevalence levels as low as π=10−6\pi=10^{-6} presents significant computational challenges. With a fixed target of n+=20n\_{+}=20 positive events per replication, the implied number of negative observations required to maintain the prevalence ratio is approximately 2020 million. Storing, sorting, and processing vectors of this size for thousands of Monte Carlo replications creates memory bottlenecks that can impede efficient analysis.

To address this, the simulation framework employs a *Weighted Downsampling Strategy* that preserves the statistical properties of the full sample while reducing memory usage by approximately 90%.

### B.1 Weighted Data Generation

Let Nreq=n+​(1−π)/πN\_{\mathrm{req}}=n\_{+}(1-\pi)/\pi be the required number of negative observations to achieve the target prevalence π\pi. We define a computational capacity constraint Ncap=2×106N\_{\mathrm{cap}}=2\times 10^{6}. The actual number of simulated negatives n−n\_{-} and their associated weights w−w\_{-} are determined as follows:

* •

  Positives: Simulate n+n\_{+} observations from the conditional distribution F1F\_{1}. Assign each a weight w+=1w\_{+}=1.
* •

  Negatives:

  + –

    If Nreq≤NcapN\_{\mathrm{req}}\leq N\_{\mathrm{cap}}, simulate NreqN\_{\mathrm{req}} observations from F0F\_{0}. Assign each a weight w−=1w\_{-}=1.
  + –

    If Nreq>NcapN\_{\mathrm{req}}>N\_{\mathrm{cap}}, simulate NcapN\_{\mathrm{cap}} observations from F0F\_{0}. Assign each a weight w−=NreqNcapw\_{-}=\frac{N\_{\mathrm{req}}}{N\_{\mathrm{cap}}}.

### B.2 Metric Calculation via Weighted Counts

Confusion matrix components are calculated using the weighted cumulative sums of the observations sorted by score. Let y(i)y\_{(i)} be the binary label and w(i)w\_{(i)} be the weight of the ii-th observation in the sorted sequence. The weighted True Positives (T​PwTP\_{w}) and False Positives (F​PwFP\_{w}) at rank kk are calculated as:

|  |  |  |
| --- | --- | --- |
|  | T​Pw​(k)=∑i=1k𝕀​(y(i)=1)⋅w(i),F​Pw​(k)=∑i=1k𝕀​(y(i)=0)⋅w(i).TP\_{w}(k)=\sum\_{i=1}^{k}\mathbb{I}(y\_{(i)}=1)\cdot w\_{(i)},\quad FP\_{w}(k)=\sum\_{i=1}^{k}\mathbb{I}(y\_{(i)}=0)\cdot w\_{(i)}. |  |

The TPR and FPR are then computed as T​Pw​(k)/∑w+TP\_{w}(k)/\sum w\_{+} and F​Pw​(k)/∑w−FP\_{w}(k)/\sum w\_{-}, respectively. Because the downsampling is uniform within the negative class, F​PwFP\_{w} is an unbiased estimator of the false positive count in the full population. This approach ensures that the resulting ROC curves, thresholds, and metric evaluations are statistically indistinguishable from the full-sample case while fitting within standard RAM constraints.

## C Simulation Details

This appendix documents the simulation framework supporting Section 6 of the paper.
The objective is to evaluate the behaviour of traditional threshold-based metrics and
Rare-Event-Stable (RES) metrics across orders of magnitude variation in event
prevalence. The design ensures a controlled environment in which any instability or
collapse of a metric can be attributed to its structural properties rather than to
sampling noise or model misspecification.

### C.1 Data-Generating Process

Each simulation draws observations from fully specified conditional forecast
distributions:

|  |  |  |
| --- | --- | --- |
|  | η​(X)∣Y=1∼F1,η​(X)∣Y=0∼F0,\eta(X)\mid Y=1\sim F\_{1},\qquad\eta(X)\mid Y=0\sim F\_{0}, |  |

where η​(X)∈(0,1)\eta(X)\in(0,1) is the model-implied score.

Two regimes of tail discrimination are considered:

* •

  Moderate separation:

  |  |  |  |
  | --- | --- | --- |
  |  | F1=Beta​(5,3),F0=Beta​(2,8).F\_{1}=\mathrm{Beta}(5,3),\qquad F\_{0}=\mathrm{Beta}(2,8). |  |
* •

  Strong separation:

  |  |  |  |
  | --- | --- | --- |
  |  | F1=Beta​(8,2),F0=Beta​(1,12).F\_{1}=\mathrm{Beta}(8,2),\qquad F\_{0}=\mathrm{Beta}(1,12). |  |

These distributions satisfy the monotone-likelihood-ratio condition and permit precise
control over the degree of overlap between the positive and negative classes.

### C.2 Prevalence Levels and Sample Sizes

Event prevalence varies over five orders of magnitude:

|  |  |  |
| --- | --- | --- |
|  | π∈{10−2, 10−3, 10−4, 10−5, 10−6}.\pi\in\{10^{-2},\,10^{-3},\,10^{-4},\,10^{-5},\,10^{-6}\}. |  |

To isolate prevalence effects while avoiding resampling noise:

* •

  For π≥10−5\pi\geq 10^{-5}, each replication includes n+=100n\_{+}=100 positive cases.
* •

  For π≤10−5\pi\leq 10^{-5}, each replication includes n+=20n\_{+}=20 positive cases.

Given n+n\_{+}, the number of negative observations is

|  |  |  |
| --- | --- | --- |
|  | n−(π)=⌊n+1−ππ⌉,n\_{-}(\pi)=\left\lfloor n\_{+}\,\frac{1-\pi}{\pi}\right\rceil, |  |

so that total sample size scales approximately as 1/π1/\pi, matching the geometry of
rare-event environments encountered in credit risk, fraud detection and reliability
engineering.

### C.3 Monte Carlo Structure

For each pair of (signal regime, prevalence), the experiment performs

|  |  |  |
| --- | --- | --- |
|  | R=2,000R=2{,}000 |  |

independent Monte Carlo replications.
For each replication:

1. 1.

   Draw n+n\_{+} samples from F1F\_{1} and n−n\_{-} samples from F0F\_{0}.
2. 2.

   Sort all scores in decreasing order.
3. 3.

   Construct the full confusion-matrix path by evaluating (TPR​(δ),FPR​(δ))(\mathrm{TPR}(\delta),\mathrm{FPR}(\delta))
   at each distinct threshold.
4. 4.

   Evaluate all metrics along this path.
5. 5.

   Record the optimal threshold δ∗\delta^{\ast} for each metric.

This produces full empirical distributions of optimal thresholds and metric values at
each prevalence level.

### C.4 Metrics Evaluated

The simulation compares the following metrics:

* •

  F1-score

  |  |  |  |
  | --- | --- | --- |
  |  | F​1​(δ)=2​Prec​(δ)​TPR​(δ)Prec​(δ)+TPR​(δ).F1(\delta)=\frac{2\,\mathrm{Prec}(\delta)\,\mathrm{TPR}(\delta)}{\mathrm{Prec}(\delta)+\mathrm{TPR}(\delta)}. |  |
* •

  Balanced Accuracy

  |  |  |  |
  | --- | --- | --- |
  |  | BA​(δ)=12​(TPR​(δ)+TNR​(δ)).\mathrm{BA}(\delta)=\tfrac{1}{2}\left(\mathrm{TPR}(\delta)+\mathrm{TNR}(\delta)\right). |  |
* •

  AUC (ROC)
  Computed when N<106N<10^{6}; omitted otherwise for computational efficiency.
* •

  RES metric for selected preference levels:

  |  |  |  |
  | --- | --- | --- |
  |  | MRE​(δ;α)=TPR​(δ)α​FPR​(δ)+(1−α),α∈{0.10, 0.50}.M\_{\mathrm{RE}}(\delta;\alpha)=\frac{\mathrm{TPR}(\delta)}{\alpha\,\mathrm{FPR}(\delta)+(1-\alpha)},\qquad\alpha\in\{0.10,\,0.50\}. |  |

Optimal thresholds are defined as

|  |  |  |
| --- | --- | --- |
|  | δ∗=arg⁡maxδ⁡M​(δ),\delta^{\ast}=\arg\max\_{\delta}M(\delta), |  |

with ties broken in favour of the smallest threshold.

## D Application: Credit-Default Forecasting

This appendix describes the empirical environment used in Section 7. The objective is
to evaluate the behaviour of classical and Rare-Event-Stable (RES) metrics in a real
credit-risk setting, where default events are rare and forecast distributions exhibit
substantial upper-tail concentration.

### D.1 Data

The analysis relies on the Give Me Some Credit consumer-credit dataset,
a widely used benchmark containing borrower characteristics and a binary indicator of
serious delinquency within two years. After removing non-informative fields and
applying median imputation to missing numeric entries, the resulting dataset contains
only predictive covariates and the binary outcome.

A stratified split allocates 70% of observations to the training set and 30% to the
test set while preserving the empirical default rate (≈6.7%\approx 6.7\%). All metric
evaluations and calibrations use out-of-sample predicted probabilities from the test
set.

### D.2 Forecasting Model

Probability-of-default forecasts are generated using a LightGBM model. Table [D.1](https://arxiv.org/html/2512.00916v1#A4.T1 "Table D.1 ‣ D.2 Forecasting Model ‣ D Application: Credit-Default Forecasting ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts") lists the exact hyperparameters used in the analysis. These values were selected to ensure a stable, monotonic score distribution typical of credit risk models, avoiding aggressive overfitting.

Table D.1: LightGBM Hyperparameters used in the empirical forecasting model.

|  |  |  |
| --- | --- | --- |
| Parameter | Value | Justification |
| objective | binary | Standard Log-Loss minimization |
| learning\_rate | 0.05 | Conservative learning rate for stability |
| num\_leaves | 31 | Limits interactions to prevent overfitting |
| bagging\_fraction | 0.8 | Stochastic subsampling for robustness |
| bagging\_freq | 1 | Frequency of bagging (every iteration) |
| nrounds | 450 | Determined via early stopping analysis |

Denote the test-set probability forecasts by p^i\widehat{p}\_{i} and the corresponding
default indicators by YiY\_{i}.

### D.3 Controlled Prevalence Regimes

To study performance under increasing rarity, additional evaluation regimes are
constructed by down-sampling positive test-set cases while retaining all negatives.
Given a target prevalence πtarget\pi\_{\mathrm{target}}, the required number of positive
observations is

|  |  |  |
| --- | --- | --- |
|  | n+=πtarget1−πtarget​n−.n\_{+}=\frac{\pi\_{\mathrm{target}}}{1-\pi\_{\mathrm{target}}}\,n\_{-}. |  |

If n+n\_{+} exceeds the available positive observations, the regime defaults to the full
test set. The analysis uses the following target prevalences:

|  |  |  |
| --- | --- | --- |
|  | {0.001, 0.005, 0.010, 0.020,empirical prevalence}.\{0.001,\;0.005,\;0.010,\;0.020,\;\text{empirical prevalence}\}. |  |

This design generates realistic low-prevalence environments while preserving the score
distribution of the forecasting model.

### D.4 Bootstrap Framework

Within each prevalence regime, 500500 bootstrap samples of fixed size are drawn. For
each bootstrap replication:

1. 1.

   Sort predicted probabilities p^i\widehat{p}\_{i} in descending order.
2. 2.

   Construct the confusion-matrix path (TPR​(δ),FPR​(δ))(\mathrm{TPR}(\delta),\mathrm{FPR}(\delta)) along all
   distinct thresholds.
3. 3.

   Evaluate each metric at each threshold.
4. 4.

   Record the optimal threshold δ∗\delta^{\ast} for each metric.

This produces empirical distributions of both metric values and optimal thresholds
across prevalence levels, enabling direct comparison between methods and identifying
threshold instability or collapse.

## E Calibration of the Policy Parameter α\alpha

This appendix describes general procedures for calibrating the RES policy parameter
α\alpha. While the implementation threshold δ∗\delta^{\ast} adapts to the empirical
forecast distribution, α\alpha encodes a stable institutional preference concerning
the marginal trade-off between false positives and false negatives.

### E.1 Cost-Based Calibration

If false-positive and false-negative errors have explicit institutional costs
CFPC\_{\mathrm{FP}} and CFNC\_{\mathrm{FN}}, the RES marginal trade-off implies:

|  |  |  |
| --- | --- | --- |
|  | α1−α=CFPCFN⟹α=CFPCFP+CFN.\frac{\alpha}{1-\alpha}=\frac{C\_{\mathrm{FP}}}{C\_{\mathrm{FN}}}\quad\Longrightarrow\quad\alpha=\frac{C\_{\mathrm{FP}}}{C\_{\mathrm{FP}}+C\_{\mathrm{FN}}}. |  |

Algorithm 1  Cost-Based Calibration of α\alpha

Misclassification costs (CFP,CFN)(C\_{\mathrm{FP}},C\_{\mathrm{FN}})

Compute r=CFP/(CFP+CFN)r=C\_{\mathrm{FP}}/(C\_{\mathrm{FP}}+C\_{\mathrm{FN}})

return α∗=r\alpha^{\ast}=r

### E.2 Calibration to a Historical Threshold

Institutions often use legacy probability-of-default cutoffs such as
δhist=0.05\delta\_{\mathrm{hist}}=0.05.
Calibration selects α\alpha such that the induced RES-optimal threshold satisfies
δRE∗​(α)≈δhist\delta^{\ast}\_{\mathrm{RE}}(\alpha)\approx\delta\_{\mathrm{hist}}.

Algorithm 2  Calibration to a Historical Threshold

Scores ηi\eta\_{i}, labels YiY\_{i}, target threshold δhist\delta\_{\mathrm{hist}}

Construct confusion-matrix path (TPR​(δ),FPR​(δ))(\mathrm{TPR}(\delta),\mathrm{FPR}(\delta))

for α\alpha in grid 𝒜\mathcal{A} do

Compute MRE​(δ;α)M\_{\mathrm{RE}}(\delta;\alpha) along the path

Set δ∗​(α)=arg⁡maxδ⁡MRE​(δ;α)\delta^{\ast}(\alpha)=\arg\max\_{\delta}M\_{\mathrm{RE}}(\delta;\alpha)

end for

return α∗=arg⁡minα⁡|δ∗​(α)−δhist|\alpha^{\ast}=\arg\min\_{\alpha}|\delta^{\ast}(\alpha)-\delta\_{\mathrm{hist}}|

### E.3 Calibration to an Intervention Rate

If the institution can process at most
rtargetr\_{\mathrm{target}} fraction of alerts, calibration requires matching the induced alarm rate
r​(α)=Pr⁡(ηi≥δRE∗​(α))r(\alpha)=\Pr(\eta\_{i}\geq\delta^{\ast}\_{\mathrm{RE}}(\alpha)).

Algorithm 3  Calibration to an Intervention-Rate Constraint

Scores ηi\eta\_{i}, labels YiY\_{i}, intervention target rtargetr\_{\mathrm{target}}

Construct confusion-matrix path (TPR​(δ),FPR​(δ))(\mathrm{TPR}(\delta),\mathrm{FPR}(\delta))

for α\alpha in grid 𝒜\mathcal{A} do

Compute δ∗​(α)\delta^{\ast}(\alpha)

Compute r​(α)=Pr⁡(ηi≥δ∗​(α))r(\alpha)=\Pr(\eta\_{i}\geq\delta^{\ast}(\alpha))

end for

return α∗=arg⁡minα⁡|r​(α)−rtarget|\alpha^{\ast}=\arg\min\_{\alpha}|r(\alpha)-r\_{\mathrm{target}}|

### E.4 Loss-Based Calibration

For an institutional loss function
L​(δ)=CFN​(1−TPR​(δ))+CFP​FPR​(δ)L(\delta)=C\_{\mathrm{FN}}(1-\mathrm{TPR}(\delta))+C\_{\mathrm{FP}}\,\mathrm{FPR}(\delta),
the optimal decision threshold is δloss∗=arg⁡minδ⁡L​(δ)\delta^{\ast}\_{\mathrm{loss}}=\arg\min\_{\delta}L(\delta).
Calibration selects α\alpha so that the RES-optimal threshold matches this loss-optimal threshold.

Algorithm 4  Loss-Based Calibration of α\alpha

Scores ηi\eta\_{i}, labels YiY\_{i}, misclassification costs (CFP,CFN)(C\_{\mathrm{FP}},C\_{\mathrm{FN}})

Compute loss-optimal threshold δloss∗\delta^{\ast}\_{\mathrm{loss}}

for α\alpha in grid 𝒜\mathcal{A} do

Compute δ∗​(α)\delta^{\ast}(\alpha)

end for

return α∗=arg⁡minα⁡|δ∗​(α)−δloss∗|\alpha^{\ast}=\arg\min\_{\alpha}|\delta^{\ast}(\alpha)-\delta^{\ast}\_{\mathrm{loss}}|

## F Empirical Calibration and Results

This appendix presents the full numerical results from the credit-default application in Section 7.

### F.1 Calibrated Values

Applying the three selected calibration methods to the LightGBM probability forecasts yields the following estimates (see Table [F.1](https://arxiv.org/html/2512.00916v1#A6.T1 "Table F.1 ‣ F.1 Calibrated Values ‣ F Empirical Calibration and Results ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts")).

Table F.1: Calibrated values of α\alpha and induced thresholds.

|  |  |  |
| --- | --- | --- |
| Scenario | Calibrated α\alpha | Induced Threshold |
| A: Historical (5%) | 0.56 | 0.05 |
| B: Capacity (3%) | 0.99 | 0.46 |
| C: Loss (1:20) | 0.05 | 0.01 |

* •

  Historical-threshold calibration: α^A=0.56\widehat{\alpha}\_{A}=0.56.
* •

  Intervention-rate calibration: α^B=0.99\widehat{\alpha}\_{B}=0.99.
* •

  Loss-based calibration: α^C=0.05\widehat{\alpha}\_{C}=0.05.

The empirically calibrated value α^C=0.05\widehat{\alpha}\_{C}=0.05 aligns closely with the theoretical optimum derived from the cost ratio 1:201:20, which implies a theoretical α=1/(1+20)≈0.048\alpha=1/(1+20)\approx 0.048. This confirms that the RES metric correctly internalizes the provided asymmetric cost structure.

### F.2 Prevalence Regimes

The following table details the exact sample sizes used for the down-sampling regimes.

Table F.2: Prevalence regimes used for the empirical evaluation.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Target π\pi | Empirical π\pi | NtotalN\_{\text{total}} | N+N\_{+} | N−N\_{-} |
| 0.0010 | 0.0010 | 42056 | 42 | 42014 |
| 0.0050 | 0.0050 | 42225 | 211 | 42014 |
| 0.0100 | 0.0100 | 42438 | 424 | 42014 |
| 0.0200 | 0.0200 | 42871 | 857 | 42014 |
| 0.0664 | 0.0664 | 45000 | 2986 | 42014 |

### F.3 Stability Analysis Tables

Tables [F.3](https://arxiv.org/html/2512.00916v1#A6.T3 "Table F.3 ‣ F.3 Stability Analysis Tables ‣ F Empirical Calibration and Results ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts") and [F.4](https://arxiv.org/html/2512.00916v1#A6.T4 "Table F.4 ‣ F.3 Stability Analysis Tables ‣ F Empirical Calibration and Results ‣ An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts") report the stability metrics for Classical and RES approaches, respectively.

Table F.3: Classical metrics: threshold stability across regimes.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Metric | Min | Max | Range | CV |
| Balanced Accuracy | 0.02 | 0.19 | 0.17 | 0.26 |
| F1-Score | 0.16 | 0.71 | 0.55 | 0.34 |
| MCC | 0.07 | 0.71 | 0.64 | 0.40 |




Table F.4: RES metrics: stability profiles across regimes.

|  |  |  |  |
| --- | --- | --- | --- |
| α\alpha | Mean Threshold | Threshold CV | MRE CV |
| 0.10 | 0.01 | 0.52 | 0.01 |
| 0.25 | 0.02 | 0.38 | 0.02 |
| 0.50 | 0.04 | 0.35 | 0.05 |




Table F.5: Operational guidance under extreme imbalance.

|  |  |  |  |
| --- | --- | --- | --- |
| Metric | Range | CV | Recommendation |
| Balanced Accuracy | 0.174 | 0.26 | Symmetric Only |
| F1-Score | 0.547 | 0.34 | Avoid (High Drift) |
| MCC | 0.641 | 0.40 | Avoid (High Drift) |
| RES (α=0.10\alpha{=}0.10) | 0.031 | 0.52 | Recommended (Stable) |
| RES (α=0.25\alpha{=}0.25) | 0.077 | 0.38 | Recommended (Stable) |
| RES (α=0.50\alpha{=}0.50) | 0.157 | 0.35 | Recommended (Stable) |

* •

  Note: A higher CV for RES δ∗\delta^{\ast} can remain operationally acceptable because the absolute thresholds stay within a narrow interior band (e.g., 0.010.01–0.050.05). Variability at this scale does not materially alter review volumes, unlike classical metrics whose thresholds drift toward degenerate extremes.

## G Additional Figures: Simulation Diagnostics

This appendix contains the supplementary diagnostic figures associated with the Simulation Study (Section 6).

![Refer to caption](x9.png)


Figure G.1: Simulation Series A1: Classical Threshold Collapse. Comparison of threshold drift for F1-score, MCC, and Balanced Accuracy across five orders of magnitude in prevalence.

![Refer to caption](x10.png)


Figure G.2: Simulation Series A2: F1 Threshold Distributions. Bootstrap histograms of optimal F1 thresholds showing increasing dispersion and multi-modality as prevalence declines.

![Refer to caption](x11.png)


Figure G.3: Simulation Series A4-a: RES Metric Value Stability. Violin plots of the maximised RES metric value M​(δ∗)M(\delta^{\ast}) across prevalence regimes. Unlike classical metrics which decay or saturate, RES values remain strictly bounded and distinct for each α\alpha, preserving discriminative signal strength even at π=10−6\pi=10^{-6}.

![Refer to caption](x12.png)


Figure G.4: Simulation Series A4-b: Geometry of RES Optimisation. Scatter plots of optimal threshold δ∗\delta^{\ast} vs. maximum metric value. The data reveal strictly stratified operating bands, demonstrating that α\alpha effectively separates institutional preferences from stochastic sampling variation.

![Refer to caption](x13.png)


Figure G.5: Simulation Series A3: RES Threshold Paths (α=0.25\alpha=0.25). Optimal RES thresholds remain strictly interior and stable across all prevalence regimes.

![Refer to caption](x14.png)


Figure G.6: Simulation Series A4: Stability Diagnostics. Coefficient of Variation (CV) of the optimal threshold for Classical vs RES metrics.

![Refer to caption](x15.png)


Figure G.7: Simulation Series A5: Threshold Heatmap. Evolution of the mean optimal threshold as a function of metric and prevalence.

## H Additional Figures: Application Diagnostics

This appendix contains the supplementary diagnostic figures associated with the Empirical Application (Section 7).

![Refer to caption](x16.png)


Figure H.1: Application Series D1: Classical Threshold Collapse. Empirical threshold drift for F1, MCC, and Balanced Accuracy across prevalence regimes.

![Refer to caption](x17.png)


Figure H.2: Application Series D2: RES Stability. RES threshold paths for α∈{0.10,0.25,0.50}\alpha\in\{0.10,0.25,0.50\} across empirical prevalence regimes.

![Refer to caption](x18.png)


Figure H.3: Application Series D3: Within-Regime Volatility. Coefficient of variation of classical metric thresholds within each prevalence regime.

![Refer to caption](x19.png)


Figure H.4: Application Series F1: Rare-Regime Instability. Bootstrap distribution of F1-optimal thresholds in the rarest regime (π≈0.001\pi\approx 0.001).

![Refer to caption](x20.png)


Figure H.5: Application Series D4: Conditional Score Distributions. Density of LightGBM predicted probabilities for defaults (Y=1Y=1) and non-defaults (Y=0Y=0) in the test set. The overlap between classes confirms that the empirical setup represents a realistic, non-separable credit risk problem, justifying the need for a calibrated decision threshold.

## I Reproducibility and Code Availability

All simulation code, empirical analysis scripts, and data-preprocessing routines used
in the preparation of this article are provided in the author data and code repository
accompanying the submission. The repository includes:

* •

  Simulation Scripts:
  All routines required to reproduce the rare-event experiments of Section 6,
  including the full data-generating processes, threshold-path construction,
  metric evaluation, and summary-statistic generation.
* •

  Credit-Default Application Scripts:
  The complete analysis pipeline for Section 7, including data cleaning, LightGBM
  probability-of-default forecasting, construction of controlled prevalence regimes,
  and bootstrap evaluation of all metrics.
* •

  Calibration Scripts:
  The code used to implement the calibration procedures described in Appendix E
  and applied empirically in Appendix F.
* •

  Figure and Table Generation:
  Scripts producing all figures and tables in the main text and Appendices.
* •

  All diagnostic figures referenced in the main text and appendix are generated automatically by the provided scripts and can be reproduced end-to-end using the repository workflow.

## J Notation and Acronyms

This appendix summarises the notation and the abbreviations used throughout the paper.
All notation refers to binary classification with probabilistic forecasts
η​(x)∈[0,1]\eta(x)\in[0,1] and threshold-based alarm rules
𝟏​{η​(x)≥δ}\mathbf{1}\{\eta(x)\geq\delta\}.

### J.1 Notation

Table J.1: Notation Summary

|  |  |
| --- | --- |
| Symbol | Meaning |
| Y∈{0,1}Y\in\{0,1\} | Binary outcome (1 = event). |
| XX | Feature vector. |
| η​(x)\eta(x) | Predicted probability or score. |
| π=Pr⁡(Y=1)\pi=\Pr(Y=1) | Event prevalence. |
| δ\delta | Alarm threshold. |
| δ∗\delta^{\ast} | Metric-induced optimal threshold. |
| TP,FP,TN,FN\mathrm{TP},\mathrm{FP},\mathrm{TN},\mathrm{FN} | Confusion-matrix components. |
| TPR​(δ)\mathrm{TPR}(\delta) | True positive rate. |
| FPR​(δ)\mathrm{FPR}(\delta) | False positive rate. |
| TNR​(δ)\mathrm{TNR}(\delta) | Specificity (1−FPR1-\mathrm{FPR}). |
| Prec​(δ)\mathrm{Prec}(\delta) | Precision. |
| F1​(t),F0​(t)F\_{1}(t),F\_{0}(t) | Conditional CDFs of η​(X)\eta(X) given Y=1Y=1 or 0. |
| f1​(t),f0​(t)f\_{1}(t),f\_{0}(t) | Conditional densities. |
| Λ​(t)\Lambda(t) | Likelihood ratio f1​(t)/f0​(t)f\_{1}(t)/f\_{0}(t). |
| α\alpha | RES policy preference parameter. |
| MRE​(δ)M\_{\mathrm{RE}}(\delta) | RES metric. |
| CFP,CFNC\_{\mathrm{FP}},C\_{\mathrm{FN}} | False-positive / false-negative costs. |
| δloss∗\delta^{\ast}\_{\text{loss}} | Loss-minimising threshold. |

### J.2 Acronyms

Table J.2: Acronyms Used in the Paper

|  |  |
| --- | --- |
| Acronym | Definition |
| AUC | Area Under the ROC Curve. |
| AUPRC | Area Under the Precision–Recall Curve. |
| BA | Balanced Accuracy. |
| CV | Coefficient of Variation. |
| FNR | False Negative Rate. |
| FPR | False Positive Rate. |
| MCC | Matthews Correlation Coefficient. |
| PD | Probability of Default. |
| RES | Rare-Event-Stable metrics. |
| ROC | Receiver Operating Characteristic. |
| TNR | True Negative Rate. |
| TPR | True Positive Rate. |