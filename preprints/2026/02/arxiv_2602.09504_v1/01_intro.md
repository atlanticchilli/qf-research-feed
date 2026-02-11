---
authors:
- Sean Cao
- Wei Jiang
- Hui Xu
doc_id: arxiv:2602.09504v1
family_id: arxiv:2602.09504
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank
  seminar participants at the University of Connecticut, the University of Maryland,
  Lancaster University, the University of California–Riverside, Singapore Management
  University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges
  support from the Smith AI Initiative for Capital Markets Research at the University
  of Maryland.'
url_abs: http://arxiv.org/abs/2602.09504v1
url_html: https://arxiv.org/html/2602.09504v1
venue: arXiv q-fin
version: 1
year: 2026
---


Sean Cao
  
Jiang Wei
  
Hui Xu
  

Sean Cao
  
University of Maryland
  
Robert H. Smith School of Business, University of Maryland, College Park. Email: [scao824@umd.edu](mailto:scao824@umd.edu)
  
Wei Jiang
  
Emory University
  
Goizueta Business School, Emory University. Email: [wei.jiang@emory.edu](mailto:wei.jiang@emory.edu)
  
Hui Xu
  
Lancaster University
Lancaster University Management School, Lancaster University. Email: [h.xu10@lancaster.ac.uk](mailto:h.xu10@lancaster.ac.uk)

(
Last updated )

###### Abstract

This research explores how human-defined goals influence the behavior of Large Language Models (LLMs) through purpose-conditioned cognition. Using financial prediction tasks, we show that revealing the downstream use (e.g., predicting stock returns or earnings) of LLM outputs leads the LLM to generate biased sentiment and competition measures, even though these measures are intended to be downstream task–independent. Goal-aware prompting shifts intermediate measures toward the disclosed downstream objective. This purpose leakage improves performance before the LLM’s knowledge cutoff, but with no advantage post-cutoff. AI bias due to “seeing the goal” is not an algorithmic flaw, but stems from human accountability in research design to ensure the statistical validity and reliability of AI-generated measurements.

Keywords: Algorithmic Bias, Purpose-Conditioned Cognition, Human Accountability, Prompt Engineering

## 1 Introduction

In organizational settings, the disclosure of downstream use can alter the nature of an intermediate task. Consider a human assistant asked to summarize interview transcripts post hoc. If told that the summaries will be used to evaluate recruiting effectiveness, the assistant may emphasize the strengths and “bright spots” of candidates who ultimately receive offers, while downplaying uncertainty, mixed signals, or unfavorable assessments. The resulting summaries support a narrative of successful recruitment, yet are less faithful to the underlying interviews. This behavioral shift reflects rational adaptation to perceived downstream purpose rather than error or lack of effort. More broadly, when intermediate tasks are conditioned on their eventual application, neutrality can be compromised even in the absence of explicit incentives.

Purpose-conditioned cognition is a well-documented human traits.111Related ideas appear in the literature on motivated reasoning and belief distortion (Bénabou and Tirole, [2016](https://arxiv.org/html/2602.09504v1#bib.bib20 "Mindful economics: the production, consumption, and value of beliefs")), framing effects in decision-making (Tversky and Kahneman, [1981](https://arxiv.org/html/2602.09504v1#bib.bib21 "The framing of decisions and the psychology of choice")) and the limits of attention and interpretation in complex environments (Mullainathan et al., [2008](https://arxiv.org/html/2602.09504v1#bib.bib22 "Coarse thinking and persuasion")). While the terminology differs across fields, these studies share the insight that cognition and interpretation are systematically shaped by perceived objectives and contextual framing. Individuals often adjust interpretation and judgment in response to perceived goals or downstream use, even without explicit incentives; and such behavior is difficult to eliminate. As a result, human-generated intermediate outputs are understood to embed goal-related distortions. On the other hand, one might expect algorithmic systems, including large language models (LLMs), to be immune from human biases. This presumption motivates a natural question: does purpose-conditioned behavior also arise in LLMs? In other words, if we restrict AI to “assistant” roles, does this separation from the final decision task ensure neutral and unbiased intermediate outputs?

Our research design addresses this question by holding the input text, model, and scoring task fixed, while varying only whether the downstream use of the output is disclosed. Specifically, we prompt a large language model to generate numerical measures of sentiment and competition intensity from the same source information (earnings call transcripts) but under two prompt conditions. In the goal-blind condition, the model is asked to produce a score without any reference to its eventual use. In the goal-aware condition, the model is informed that its output will be used to predict future stock returns or earnings. This design therefore isolates the effect of disclosing downstream use on the model’s intermediate outputs.

Disclosing downstream use materially alters both the statistical properties and the economic content of LLM-generated sentiment scores. In standard portfolio-sorting tests, goal-aware sentiment produces substantially larger return spreads than goal-blind sentiment prior to the model’s knowledge cutoff. This pattern suggests that the model conditions its intermediate outputs on the disclosed objective and implicitly re-weights return-relevant patterns learned during training. The relative advantage of the goal-aware regime disappears after the knowledge cutoff, indicating that the earlier performance gap is tied to information availability rather than a stable improvement in signal quality.

This comparison of the two prompt regimes is further confirmed in Fama and MacBeth ([1973](https://arxiv.org/html/2602.09504v1#bib.bib4 "Risk, return, and equilibrium: empirical tests")) return-prediction regressions. Intermediate variables generated under goal-aware prompts exhibit stronger incremental predictive power than those from the goal-blind regime in the pre-cutoff period, both in coefficient significance and in out-of-sample R2R^{2}. Once the model no longer has access to future information beyond the cutoff, this advantage dissipates. Together, these results are consistent with objective-conditioned output adjustment rather than a structurally more informative sentiment measure. In fact, the enhanced goodness-of-fit prior to knowledge cutoff even degrade out-of-sample model generalization.

The seeming goal-conditioning behavior of a cold-blooded algorithm has its roots in how AI systems are trained and deployed. Large language models are optimized to generate outputs that satisfy the objective implied by the prompt, conditional on their learned representations. Disclosing downstream use alters this implicit objective, encouraging responses that align with anticipated evaluation criteria rather than with neutral processing of the input. This behavior does not require intent or explicit embedding of forward-looking information. Instead, it reflects the model’s reliance on correlations learned during training and its sensitivity to contextual cues about what constitutes a desirable output. As a result, goal awareness can improve in-sample alignment while reducing robustness when the information environment changes.

Our study contributes to the AI and LLM methodology literature (reviewed in Appendix [\thechapter.A](https://arxiv.org/html/2602.09504v1#X.A1 "Appendix \thechapter.A Literature Review ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.")) in two distinct ways. First, existing research largely attributes AI bias to algorithmic limitations. Look-ahead bias and memorization, for example, are commonly traced to models’ access to unintended training data (Glasserman and Lin, [2023](https://arxiv.org/html/2602.09504v1#bib.bib8 "Assessing look-ahead bias in stock return predictions generated by gpt sentiment analysis"); Sarkar and Vafa, [2024](https://arxiv.org/html/2602.09504v1#bib.bib1 "Lookahead bias in pretrained language models"); Lopez-Lira, Tang, and Zhu, [2025](https://arxiv.org/html/2602.09504v1#bib.bib9 "The memorization problem: can we trust llms’ economic forecasts?"); He, Lv, Manela, and Wu, [2025](https://arxiv.org/html/2602.09504v1#bib.bib7 "Chronologically consistent large language models"); Cao, Wang, and Xiang, [2025](https://arxiv.org/html/2602.09504v1#bib.bib29 "When llm go abroad: foreign bias in ai financial predictions")). Moving beyond these training data-centric issues, AI has also been criticized for potential biases in exploration strategies and model weights, which may be related to ethical concerns (Fedyk et al., [2024](https://arxiv.org/html/2602.09504v1#bib.bib24 "AI and perception biases in investments: an experimental study")) and preference alignment (Ouyang et al., [2024](https://arxiv.org/html/2602.09504v1#bib.bib11 "AI as decision-maker: risk preferences of llms"); Hirshleifer et al., [2025](https://arxiv.org/html/2602.09504v1#bib.bib30 "Social finance in the age of ai: a tale of two platforms")). Our analysis shifts the focus from these machine-level limitations to human use of machine. We show that human disclosure of downstream task (e.g., return and earnings predictions) reshapes intermediate outputs (e.g., sentiment and competition measures) in ways that inflate the downstream task performance. Ultimately, this leads to impressive in-sample results that fail to generalize out-of-sample.

The second contribution of the paper is to isolate goal awareness from other AI biases, which naturally emerge when LLMs are deployed directly on end tasks such as return forecasting. A commonly proposed safeguard is to limit LLMs to intermediate functions, analogous to a research assistant, while reserving final predictions and decisions for human judgment. Our results show that even at the intermediate-measurement stage, disclosure of the downstream objective can introduce additional, goal-conditioned distortion in the generated signals. While the design of this study is minimalist, we want to note that goal awareness need not arise only from explicit instructions; it may also be inferred implicitly from contextual cues, prompt history, task framing, or repeated interaction patterns. Even unintentional target leakage could also allow the model to form a latent representation of the disclosed downstream objective in the construction of intermediate measures.

More broadly, the analysis clarifies the distinction between using AI as a task agent that optimizes directly toward an announced objective and using it as a measurement tool that produces inputs for subsequent human evaluation. Prompt and workflow designs that deliberately reduce objective conditioning can therefore mitigate machine-driven bias. The mechanism we uncover thus bears an analogy to the phenomenon of “AI sycophancy” discussed in recent work, e.g., Sharma et al. ([2023](https://arxiv.org/html/2602.09504v1#bib.bib23 "Towards understanding sycophancy in language models")). In both cases, large language models adjust their outputs in response to contextual cues about what constitutes a desirable response, rather than adhering to a task-invariant notion of correctness or neutrality.222In sycophancy, this adjustment manifests as alignment with a user’s stated beliefs or preferences; in our setting, it appears as alignment with an inferred evaluation objective. The underlying commonality is not intent, but sensitivity to signals about reward or approval embedded in the prompt. As a result, both phenomena illustrate how models trained to be helpful and aligned can deviate from neutral information processing when the prompt conveys implicit incentives, even in the absence of explicit instructions or forward-looking information.333In computer science, related concerns are discussed under reward hacking, specification gaming, and objective misgeneralization, where models optimize inferred proxy objectives rather than the intended task. Our setting requires no change in model parameters or rewards; the distortion arises solely from human framing at inference time. A design choice that weakens alignment with a stated downstream goal can improve statistical validity and out-of-sample reliability.

While our experimental design makes goal disclosure explicitly controlled, in practice information about downstream use is often conveyed indirectly through prior interactions, repeated prompt patterns, or contextual cues in surrounding instructions, leading the model to form cumulative belief about how its outputs will be used and evaluated. The mechanism we document therefore extends beyond the specific prompting variation studied herein. A natural implication is that intermediate variables constructed with the aid of AI should, whenever feasible, be generated under prompts that are agnostic to downstream use and evaluated using strict out-of-sample tests. Treating LLMs as neutral measurement devices requires not only holding inputs and models fixed, but also constraining the informational environment to limit objective inference by the model beyond the intrinsic requirements of the task. In this sense, the challenge is not primarily one of algorithmic bias, but of human accountability in how objectives, context, and evaluation criteria are built in the system.

## 2 Experimental Design and Data

### 2.1 LLM Propmt and Scoring

Our objective is to examine whether large language models (LLMs) systematically adjust their outputs when they are informed about the downstream task for which those outputs will ultimately be used. We focus on two economically important forecasting applications: monthly stock returns and quarterly earnings per share (EPS). In both settings, the firm’s most recent earnings call transcript serves the sole input to the LLM. Rather than asking the model to directly predict economic outcomes, we instruct it to generate an intermediate score that is subsequently used in a simple predictive regression.

* •

  Return prediction task. For each calendar month tt, the model is prompted with the most recent earnings call transcript available at t−1t-1 to generate a continuous sentiment score, ranging from -1 to 1, summarizing the firm’s business sentiment for month tt. We then use this month-tt sentiment score to predict the firm’s stock returns in month tt.
* •

  Earnings prediction task. For each fiscal quarter tt, the model is prompted with the most recent earnings call transcript available at t−1t-1 to generate a competition score, ranging from -1 to 1, which captures the intensity of competitive pressure the firm faces in quarter tt. We then use this quarter-tt competition score to predict the firm’s earnings realized in quarter tt.

A central feature of the experimental design is that the LLM does not directly forecast stock returns or earnings. Instead, it produces an intermediate construct (i.e., sentiment or competitive intensity), which we subsequently map to economic outcomes using standard econometric models. This design choice allows us to test whether the LLM adjusts these intermediate scores as if it were strategically responding to the knowledge of their downstream use. For each task, we construct two prompts that are otherwise identical in wording and structure, differing only in whether the prompt explicitly discloses the ultimate use of the generated score.

1. 1.

   Goal-Blind Prompt (control): The LLM is asked to generate the score without being told that it will be used in a forecasting regression.
2. 2.

   Goal-Aware Prompt (treatment): The LLM is informed that the score it produces will later be used as an explanatory variable in a regression to predict either stock returns or earnings.

This minimalist treatment variation allows us to cleanly isolate whether, and through what channels, an LLM alters its outputs once it becomes aware of the user’s ultimate objective. Conceptual concerns arise from anticipatory behavior, in which the model conditions its responses on inferred downstream use rather than on the stated prediction task alone; reward hacking, whereby the model optimizes for the perceived evaluation criterion instead of the intended informational objective; and goal misalignment, in which the model’s internal optimization departs from the user’s declared constraints. Importantly, these issues are examined within an economically meaningful forecasting environment, allowing deviations in model behavior to be traced to distortions in information processing rather than an abstract alignment failure.

To illustrate, the following text shows the goal-blind prompt used to generate sentiment scores:

> "For the following tasks, all dates are expressed in the format MM/DD/YYYY (month/day/year).
>   
> Below is the earnings call transcript of {ticker}. Please provide a continuous sentiment score in [-1, 1] about the firm’s business sentiment for the month ending on {date}.
>   
> Provide a precise numerical answer. Format as a JSON object with the following fields:
> - answer: The precise numerical answer to the question. No strings.
>   
> {the firm’s earnings call transcript}."

The corresponding goal-aware version differs only by the addition of a single sentence that discloses the downstream use of the output, namely the predictive task.

> "For the following tasks, all dates are expressed in the format MM/DD/YYYY (month/day/year).
>   
> Below is the earnings call transcript of {ticker}. Please provide a continuous sentiment score in [-1, 1] about the firm’s business sentiment for the month ending on {date}. The sentiment score later will be used as an explanatory variable in a regression to predict the monthly stock returns ending on {date}.
>   
> Provide a precise numerical answer. Format as a JSON object with the following fields:
> - answer: The precise numerical answer to the question. No strings.
>   
> {the firm’s earnings call transcript}."

Aside from this one sentence, all instructions, including input data, output format, and numerical constraints, remain identical across the two prompts and processes.

### 2.2 Data and LLM model

Our sample consists of S&P 500 firms over the period from January 2022 to December 2024. Earnings call transcripts are obtained from Capital IQ, which provides standardized, time-stamped transcripts for publicly listed firms. Monthly stock return data are drawn from CRSP, and accounting information, including earnings per share (EPS), is sourced from Compustat. We further use CRSP and Compustat data to construct standard firm-level control variables employed in our predictive regressions, such as the book-to-market ratio and firm size.

To generate sentiment and competition scores, we prompt the GPT-4o-mini model. GPT-4o-mini (“o” for “omni”) is a lightweight, cost-efficient language model designed for focused inference tasks with low latency. According to OpenAI, GPT-4o-mini is produced via distillation from a larger frontier model (GPT-4o), allowing it to replicate much of the larger model’s behavior at substantially lower computational cost.

Critically for our experimental design, GPT-4o-mini has a fixed knowledge cutoff of October 1, 2023. As a result, the model does not have access to information that occurs after this date. This feature is central to our analysis, as it allows us to cleanly separate changes in predictive performance driven by prompt design and goal awareness from those arising from direct access to future information.

### 2.3 Evaluation Metrics

We first evaluate the economic relevance of GPT-generated sentiment scores using portfolio-sorting tests that are standard in the asset-pricing literature. In each period, firms are sorted into quintiles based on their GPT-produced sentiment scores, and we form an equally weighted zero-investment long–short portfolio that buys firms in the highest quintile and sells firms in the lowest quintile. Portfolio performance is measured using average excess returns. The analysis is conducted separately for goal-aware and goal-blind scores. Comparing portfolio performance across the two prompt designs allows us to assess whether revealing the ultimate prediction task leads to economically stronger trading signals, and whether the relative performance of goal-aware versus goal-blind scores changes after the cutoff date.

We evaluate predictive performance using two complementary approaches: Fama and MacBeth ([1973](https://arxiv.org/html/2602.09504v1#bib.bib4 "Risk, return, and equilibrium: empirical tests")) predictive regressions and genuine out-of-sample forecasting. The first approach tests whether LLM-generated scores significantly predict returns or earnings in the full sample and how this relationship changes around the model’s knowledge cutoff. The second assesses practical forecasting accuracy by simulating real-time predictions on unseen data. Together, these methods provide a robust validation: the regressions establish statistical significance of the predictive variable, while the out-of-sample exercise determines whether this significance translates into reliable practical performance.

We use standard cross-sectional predictive regressions to examine statistical predictability. For stock returns, we implement the Fama and MacBeth ([1973](https://arxiv.org/html/2602.09504v1#bib.bib4 "Risk, return, and equilibrium: empirical tests")) methodology and estimate monthly cross-sectional regressions of the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ri,t=\displaystyle R\_{i,t}= | β1,t​Scorei,t−1×Pre​-​Cutofft+β2,t​Scorei,t−1×Post​-​Cutofft+\displaystyle\beta\_{1,t}\mathrm{Score}\_{i,t-1}\times\mathrm{Pre\text{-}Cutoff}\_{t}+\beta\_{2,t}\mathrm{Score}\_{i,t-1}\times\mathrm{Post\text{-}Cutoff}\_{t}+ |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | β3,t​Diffi,t−1×Pre​-​Cutofft+β4,t​Diffi,t−1×Post​-​Cutofft+αt+ϵi,t,\displaystyle\beta\_{3,t}\mathrm{Diff}\_{i,t-1}\times\mathrm{Pre\text{-}Cutoff}\_{t}+\beta\_{4,t}\mathrm{Diff}\_{i,t-1}\times\mathrm{Post\text{-}Cutoff}\_{t}+\alpha\_{t}+\epsilon\_{i,t}, |  | (1) |

where Ri,tR\_{i,t} denotes the excess return of firm ii in month tt. S​c​o​r​ei,t−1Score\_{i,t-1} is the sentiment score generated by the goal-blind GPT prompt using the most recent earnings call transcript available at t−1t-1. D​i​f​fi,t−1Dif\!f\_{i,t-1} is the difference between the sentiment scores produced by the goal-aware and goal-blind prompts. Because the sentiment score does not have a natural scale, raw values may not be directly comparable across firms, industries, or time periods. For this reason we transform both sentiment scores into percentiles across all firms within each year–month so that the difference score captures the gap in the percentile values of scores generated under goal-aware and goal-blind scores. Correspondingly, the time-period fixed effect αt\alpha\_{t} is included to absorb aggregate time series shifts in returns.

We interact both S​c​o​r​ei,t−1Score\_{i,t-1} and D​i​f​fi,t−1Dif\!f\_{i,t-1} with indicator variables P​r​e​-​C​u​t​o​f​ftPre\text{-}Cutof\!f\_{t} and P​o​s​t​-​C​u​t​o​f​ftPost\text{-}Cutof\!f\_{t}, which equal one if month tt occurs before or after the LLM’s knowledge cutoff date, respectively. This specification allows predictive coefficients to differ across the two periods and is designed to isolate the role of goal awareness. When the LLM is goal aware, it may leverage patterns, associations, and correlations embedded in the full-sample available that are correlated with future outcomes. Because such information is internalized during training and cannot be selectively “unlearned” at inference time, goal awareness can thus induce outputs that are implicitly forward-looking relative to the evaluation period, leading to stronger predictive performance prior to the cutoff. Such behavior does not require the LLM to explicitly access forward-looking information in making predictions. Once the evaluation period extends beyond the model’s knowledge cutoff, however, these internalized correlations become equally stale, and the performance advantage of goal-aware scores over goal-blind scores should dissipate or reverse.

Accordingly, any differential predictive power attributable to goal awareness should be concentrated in the pre-cutoff period and attenuated in the post-cutoff period. For this reason, we expect β1,t\beta\_{1,t} and β2,t\beta\_{2,t} in Equation ([1](https://arxiv.org/html/2602.09504v1#S2.E1 "In 2.3 Evaluation Metrics ‣ 2 Experimental Design and Data ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.")) to be positive if the intermediate variable is informative. Moreover, the two coefficients should be of similar magnitude, as knowledge of future returns prior to the cutoff date should not matter under goal blindness. By the same reasoning, β4,t=0\beta\_{4,t}=0 since the lack of future-relevant information renders any advantage of goal awareness nil after the cutoff. Finally, β3,t\beta\_{3,t} is the key coefficient of interest. Under the null, β3,t=0\beta\_{3,t}=0 if goal awareness does not change the way the LLM generates outputs; under the alternative, β3,t\beta\_{3,t} may be positive if disclosure of the downstream use of the output motivates the LLM to produce intermediate measures that better align with the ultimate task.

For earnings outcomes, we adopt an analogous specification, replacing monthly excess returns with quarterly earnings per share (EPS). We use diluted EPS excluding extraordinary items from Compustat, following common practice in the literature. In this setting, S​c​o​r​ei,t−1Score\_{i,t-1} corresponds to the competition score generated by the goal-blind prompt, transformed into percentiles within the same 4-digit SIC industry ×\times year cohort. The difference measure captures the gap between the scores generated under the goal-blind and goal-aware prompts. This structure, which is parallel to our earlier exercise on stock returns, facilitates multiple validation by allowing us to test how goal awareness affects predictability across both financial and accounting settings.

Now we come to the stage of assessing genuine, out-of-sample forecasting performance. At the beginning of each forecast period, TT, we estimate the regression model on all data available through T−1T-1 and generate predictions for outcomes at TT; This estimation window is then expanded recursively to include an additional observation before each new forecast, ensuring that every prediction is made using the maximum available history. The unit of observation is monthly for stock returns and quarterly for earnings. For stock returns prediction, this amounts to the following predictive regression:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ri,t=α+\displaystyle R\_{i,t}=\alpha+ | γ​Scorei,t−1+ϵi,t,∀t≤T−1\displaystyle\gamma\mathrm{Score}\_{i,t-1}+\epsilon\_{i,t},\forall t\leq T-1 |  | (2) |

We then use the estimated coefficients to predict stock returns Ri,TR\_{i,T} based on sentiment scores observed at T−1T-1. We estimate this regression separately using scores generated from the goal-aware and goal-blind prompts. Earnings predictions follow an analogous specification except additional adjustment to mitigate seasonality and auto-correlation in earnings, such that we replace the EPS variable with the year-over-year (YoY) growth rate of same-quarter earnings per share, i.e., E​P​Si,TE​P​Si,T−4\frac{EPS\_{i,T}}{EPS\_{i,T-4}}.

Once we obtain model-based forecasts, we construct a forecast accuracy measure analogous to the out-of-sample (O​O​SOOS) R2R^{2}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | RO​O​S,i,T2=1−(yi,T−y^i,T)2(yT−1−yi,T)2,R^{2}\_{OOS,i,T}=1-\frac{(y\_{i,T}-\hat{y}\_{i,T})^{2}}{(y\_{T-1}-y\_{i,T})^{2}}, |  | (3) |

where yi,Ty\_{i,T} is the realized outcome, y^i,T\hat{y}\_{i,T} is the model-based forecast, and yT−1y\_{T-1} is the benchmark forecast—specifically, the simple historical cross-sectional mean of the outcome variable across all firms, calculated using data available only through period T−1T-1.

With the forecast accuracy measure at the firm-period level, we are able to assess their performance in relation to goal-awareness and interacted with the LLM knowledge cutoff date. More specifically, we estimate the following panel regression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | RO​O​S,i,T2=θ1​Goal​-​Awarei,T×Post​-​CutoffT+θ2​Goal​-​Awarei,T+θ3​Post​-​CutoffT+μi+νT+ϵi,T\displaystyle R^{2}\_{OOS,i,T}=\theta\_{1}\mathrm{Goal\text{-}Aware}\_{i,T}\times\mathrm{Post\text{-}Cutoff}\_{T}+\theta\_{2}\mathrm{Goal\text{-}Aware}\_{i,T}+\theta\_{3}\mathrm{Post\text{-}Cutoff}\_{T}+\mu\_{i}+\nu\_{T}+\epsilon\_{i,T} |  | (4) |

where G​o​a​l​-​A​w​a​r​ei,TGoal\text{-}Aware\_{i,T} is an indicator equal to one (zero) if RO​O​S,i,T2R^{2}\_{OOS,i,T} results from the goal-aware (goal-blind) regime. μi\mu\_{i} and νT\nu\_{T} denote firm and time fixed effects, respectively. Both coefficients, θ1\theta\_{1} and θ2\theta\_{2}, are of central interest, as they capture the incremental forecasting performance of goal-aware relative to goal-blind scores before and after the model’s knowledge cutoff date. A positive θ2\theta\_{2} indicates improved performance attributable to goal awareness, whereas such an effect should be absent after the knowledge cutoff, implying θ1=0\theta\_{1}=0.

## 3 Findings

### 3.1 Sentiment Scores and Stock Returns Prediction

#### 3.1.1 Portfolio Sorts and Return Performance

We begin by examining the economic implications of GPT-generated sentiment scores using portfolio-sorting tests. The purpose of this exercise is to verify that the sentiment scores have predictive content for stock returns. Although return forecasting is not a central objective of this study, the presence of a predictive variable is required to evaluate how the LLM’s output changes when the model is made aware of the downstream predictive task. Figure [1](https://arxiv.org/html/2602.09504v1#Sx1.F1 "Figure 1 ‣ Figures ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.") plots the cumulative returns to long–short portfolios formed by buying firms in the highest sentiment quintile and selling firms in the lowest sentiment quintile, separately for scores generated under goal-aware and goal-blind prompts. Table [1](https://arxiv.org/html/2602.09504v1#Sx2.T1 "Table 1 ‣ Tables ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.") reports the corresponding average monthly return spreads for the pre– and post–knowledge cutoff periods.

Prior to the knowledge cutoff, sentiment scores generated under both prompt designs exhibit economically meaningful return predictability. As reported in Table [1](https://arxiv.org/html/2602.09504v1#Sx2.T1 "Table 1 ‣ Tables ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland."), the long–short portfolio based on goal-aware sentiment earns an average monthly return spread of 1.552%, while the corresponding spread based on goal-blind sentiment is 1.069%. Both spreads are statistically significant, indicating that GPT-generated sentiment contains predictive information about future stock returns even when the ultimate objective is not fully communicated to the model. Notably, the goal-aware strategy delivers significantly stronger performance: the difference in High–Low spreads between the two regimes, 0.483 percentage point per month, is statistically significant at the 5% level. This relative outperformance is evident graphically in Figure [1](https://arxiv.org/html/2602.09504v1#Sx1.F1 "Figure 1 ‣ Figures ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland."), where cumulative returns of the goal-aware portfolio diverge upward from those of the goal-blind portfolio in the period leading up to the cutoff.

After the knowledge cutoff, both strategies continue to generate statistically significant return spreads. The monthly High–Low spread equals 2.269% for the goal-aware portfolio and 2.239% for the goal-blind portfolio, with no economically or statistically meaningful difference between the two. Confirming this result, the cumulative return paths in the upper panel of Figure [1](https://arxiv.org/html/2602.09504v1#Sx1.F1 "Figure 1 ‣ Figures ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland."), normalizing both portfolios to start from unity at the cutoff date, track each other closely in the post-cutoff period, showing no persistent advantage for the goal-aware strategy. If anything, the goal-blind long–short portfolio performs slightly better (though not statistically significant). One possible explanation is mild overfitting: making the LLM aware of the downstream objective may induce greater optimization to in-sample patterns, whereas the goal-blind specification generate more stable signals that generalize slightly better in the true out-of-sample (post-cutoff) period.

Taken together, the portfolio evidence shows a contrast around the knowledge cutoff. Before the cutoff, disclosing the downstream prediction task increases the measured economic content of GPT-generated sentiment scores. After the cutoff, this relative difference disappears, even though both prompt designs continue to exhibit statistically significant return predictability in absolute terms. This pattern indicates that the higher pre-cutoff performance of goal-aware sentiment does not arise from superior information extraction. Instead, it is consistent with goal awareness reshaping the distribution of model outputs by incorporating back-tested performance when data from the evaluation period are available during training. The absence of a post-cutoff difference helps identify the source of the pre-cutoff effect. Overall, the results highlight the importance of accounting for goal awareness when interpreting LLM-based measures in empirical studies.

#### 3.1.2 Predictive Regressions and Out-of-Sample Performance

The comparative predictive performance of the goal-aware and goal-blind regimes can also be examined within the regression framework described in Section [2.3](https://arxiv.org/html/2602.09504v1#S2.SS3 "2.3 Evaluation Metrics ‣ 2 Experimental Design and Data ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland."). Table [2](https://arxiv.org/html/2602.09504v1#Sx2.T2 "Table 2 ‣ Tables ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.") reports Fama–MacBeth estimates from monthly cross-sectional regressions of excess stock returns on GPT-generated sentiment scores, following Equation ([1](https://arxiv.org/html/2602.09504v1#S2.E1 "In 2.3 Evaluation Metrics ‣ 2 Experimental Design and Data ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.")). The specification allows the slope coefficients to differ between the goal-aware and goal-blind regimes and across the pre- and post–knowledge cutoff periods.

Across specifications, sentiment scores generated under the goal-blind prompt display economically meaningful and statistically significant predictive power both before and after the knowledge cutoff. The estimated coefficients on the goal-blind score interacted with the pre-cutoff indicator are positive and statistically significant, and their magnitudes remain similar in the post-cutoff period. Formal tests reported in the bottom panel do not reject equality between the pre- and post-cutoff coefficients for the goal-blind score.

By contrast, the incremental predictive content of goal-aware sentiment—captured by the Diff measure, exhibits a discontinuity at the knowledge cutoff. In the pre-cutoff period, the coefficient on Diff is positive and statistically significant across both specifications, indicating that goal-aware sentiment contains incremental predictive power. The magnitude prevails across firms characteristics such as size and book-to-market. After the knowledge cutoff, the Diff coefficient collapses to near-zero. Consistent with this pattern, the bottom panel reports that the equality of the pre- and post-cutoff Diff coefficients is rejected at the 5% significance levels. Altogether, the regression evidence closely mirrors the portfolio results.

Next we evaluate whether these regression-based differences carry over to out-of-sample forecasting performance as modeled in Equation ([2](https://arxiv.org/html/2602.09504v1#Sx1.F2 "Figure 2 ‣ Figures ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.")). Figure [2](https://arxiv.org/html/2602.09504v1#Sx1.F2 "Figure 2 ‣ Figures ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.") plots the monthly out-of-sample RO​O​S2R\_{OOS}^{2} obtained from forecasting next-month stock returns using sentiment scores generated under goal-aware and goal-blind prompts. In each month, we estimate predictive regressions using an expanding window (where the estimation sample grows to include all available data up to the prior month), compute out-of-sample accuracy relative to a simple historical cross-sectional mean benchmark calculated using data available only through the prior period, and average the resulting out-of-sample goodness-of-fit, RO​O​S2R\_{OOS}^{2}, across firms in each time period.

Figure [2](https://arxiv.org/html/2602.09504v1#Sx1.F2 "Figure 2 ‣ Figures ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.") reveals a distinct shift in relative predictive accuracy across the knowledge cutoff. Prior to the cutoff, the goal-aware prompt generally outperforms the goal-blind prompt. Following the cutoff, however, this relationship reverses: the performance of the goal-aware prompt deteriorates significantly, falling below that of the goal-blind benchmark.
Table [3](https://arxiv.org/html/2602.09504v1#Sx2.T3 "Table 3 ‣ Tables ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.") validates this comparison by regressing monthly RO​O​S2R\_{OOS}^{2} values on indicators for prompt regimes (goal-aware) and the knowledge cutoff dates (Post Cutoff). Consistent with the visual evidence, the coefficient on the interaction between goal-aware prompt and the post-cutoff indicator is negative and statistically significant across specifications. The magnitude of the estimate implies a meaningful reduction in out-of-sample predictive accuracy for goal-aware sentiment once the model’s knowledge becomes stale.

The comparative results of out-of-sample predictive performance complements those from portfolio sorting and direct return predictive regressions. While goal-aware sentiment appears to deliver stronger in-sample and pre-cutoff predictive signals, this advantage does not persist when evaluated under a strict out-of-sample framework after the knowledge cutoff. The pattern suggests that the superior pre-cutoff performance of goal-aware sentiment reflects, at least in part, the model’s tendency to condition its outputs on the evaluation objective in ways that do not generalize once the underlying knowledge environment changes.

Taken together, results from three complementary research designs indicate that making the downstream objective explicit can improve apparent predictive performance in-sample and prior to the knowledge cutoff, but does not improve, or may even degrade out-of-sample generalization. This pattern is consistent with goal awareness inducing objective-conditioned optimization by LLM that exploits correlations present in the training or evaluation sample rather, at the expense of extracting stable predictive structure. The findings highlight the distinction between economically meaningful signals and prompt-induced optimization artifacts when employing LLM-generated measures in empirical research.

### 3.2 Earnings Prediction with Competition Scores

#### 3.2.1 Predictive Regressions and Out-of-Sample Performance

Similar to our discussion of GPT-generated sentiment scores and their relationship with future stock returns, we first study the ability of competition-threat scores to predict future earnings. Table [4](https://arxiv.org/html/2602.09504v1#Sx2.T4 "Table 4 ‣ Tables ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.") reports Fama–MacBeth estimates from firm-quarter panel regressions of next-quarter earnings per share on GPT-generated competition scores, allowing the predictive slopes to differ between goal-aware and goal-blind regimes and across the pre– and post–knowledge cutoff periods. Results are shown in Table [4](https://arxiv.org/html/2602.09504v1#Sx2.T4 "Table 4 ‣ Tables ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").

Across specifications, competition scores generated under the goal-blind prompt are negatively associated with future earnings in the pre-cutoff period. The coefficient associate with the goal-blind score interacted with the pre-cutoff indicator are negative and statistically significant), consistent with heightened competitive pressure predicting lower subsequent earnings. This relation, nevertheless, weakens after the knowledge cutoff. Formal tests reported in the bottom panel indicate that the difference between the pre- and post-cutoff coefficients for the goal-blind score is not statistically significant at the 5% levels.

By contrast, the difference between the pre- and post-cutoff incremental predictive power associated with goal awareness is statistically significant at the 10% and 5% levels across the two specifications, suggesting that the incremental predictive performance dissipates once information about the future is no longer available. Economically, revealing the ultimate forecasting task strengthens the association between perceived competitive threats and subsequent earnings realizations, but only during the pre-cutoff when future information is accessible by the LLM.

In sum, the earnings predictions reinforce the central message: While GPT-generated competition scores exhibit economically intuitive relations with future earnings, the incremental predictive content attributable to goal awareness that is confined to the pre-cutoff period suggests that communicating downstream purpose of the intermediate output may amplify predictive relations in-sample with no out-of-sample generalization.

We conclude our analysis by examining the out-of-sample forecasting performance of GPT-generated competition scores for predicting future earnings. Figure [3](https://arxiv.org/html/2602.09504v1#Sx1.F3 "Figure 3 ‣ Figures ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.") plots quarterly average out-of-sample R2R^{2} values from expanding-window forecasts (where each forecast uses all available historical data up to the prior quarter) of earnings growth using goal-aware and goal-blind competition scores. Table [5](https://arxiv.org/html/2602.09504v1#Sx2.T5 "Table 5 ‣ Tables ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.") complements the visual evidence by reporting regression tests that quantify how predictive performance changes in the same way following the GPT knowledge cutoff.

## 4 Conclusion

This study highlights a subtle but consequential channel through which human–AI interaction can distort empirical inference. We show that even when large language models are used solely to construct intermediate variables rather than to make explicit predictions, revealing the downstream research objective systematically reshapes model outputs. The resulting bias does not arise from flawed data or model architecture, but from how the task is framed. In this sense, what appears to be “machine bias” is often better understood as a form of human-induced distortion, embedded in prompt design.

The mechanism closely parallels human behavior in organizations. When an employee or human assistant is informed about how her output will be evaluated or used as input for subsequent tasks, she may rationally optimize for the anticipated performance criterion or downstream utility rather than for the intrinsic quality of the task itself. Such awareness need not arise from explicit instruction; indirect cues, contextual framing, or accumulated experience can be sufficient to induce goal-conditioned behavior. Yet many organizational systems rely on the neutrality of intermediate outputs for overall optimality in evaluations and execution. Our findings suggest that LLMs exhibit an analogous tendency in this form of misalignment: awareness of downstream objectives can induce over-optimization that improves in-sample performance while degrading system-wide generalization. Such a lesson has direct implications for the design of credible AI-assisted research workflows.

## Figures

![Refer to caption](figures/figure_long_short_sentiment.png)


Figure 1: Cumulative Long–Short Portfolio Returns from Goal-Aware and Goal-Blind Sentiment Scores



This figure plots the cumulative returns to long–short portfolios constructed using GPT-generated sentiment scores. Each month, firms are sorted into quintiles based on their sentiment scores, separately for the goal-blind and goal-aware prompts. The portfolio goes long the highest-sentiment quintile and short the lowest-sentiment quintile, and cumulative returns are computed over time. The shaded region marks the GPT knowledge-cutoff period. To facilitate comparison of post-cutoff performance, cumulative returns after the cutoff are normalized by the value of the cumulative return in the last month prior to the cutoff. The figure illustrates how the long–short strategy based on goal-aware sentiment evolves relative to the strategy based on goal-blind sentiment before and after the knowledge cutoff.



![Refer to caption](figures/figure_r2_time_plot_sentiment.png)

Figure 2: Monthly Out-of-Sample Forecast Accuracy Using Goal-Aware and Goal-Blind Sentiment Scores

This figure shows the monthly RO​O​S2R^{2}\_{OOS} from using goal-aware vs. goal-blind sentiment to forecast stock returns. Each month we run expanding-window regressions, predict next-month returns, compute OOS accuracy relative to the historical mean, and average across firms. The plot highlights how the two prompts track each other before the cutoff and how their predictive behavior evolves once GPT’s knowledge becomes stale.

![Refer to caption](figures/figure_r2_quarterly_plot_competition.png)

Figure 3: Quarterly Out-of-Sample Forecast Accuracy Using GPT-Derived Competition Scores

We forecast quarterly earnings growth using goal-aware vs. goal-blind competition scores and compute RO​O​S2R^{2}\_{OOS} each quarter using expanding-window regressions. The plot shows how predictive accuracy evolves around the GPT knowledge cutoff: both score types weaken after the cutoff, but the decline is sharper for goal-aware scores, indicating that the task-aware component of GPT’s scoring deteriorates once the model’s information becomes stale.

## Tables

Table 1: Return Spreads from Quintile Portfolios Formed on Goal-Aware and Goal-Blind Sentiment Scores



This table reports return spreads from quintile portfolios constructed using sentiment scores generated under goal-blind and goal-aware prompts. For each month, we independently sort firms into quintiles based on (i) sentiment scores from the goal-blind GPT prompt and (ii) sentiment scores from the goal-aware prompt. We compute equal-weighted returns for the highest- and lowest-quintile portfolios and report the difference in returns (High–Low) for the pre– and post–knowledge cutoff periods. Within each row, we conduct a paired
tt-test of the High–Low spread. The last row reports paired tt-tests comparing the spreads between the goal-blind and goal-aware groups. \*\*\*, \*, and \* denote significance at the 1%, 5%, and 10% levels, respectively, based on one-sided paired tt-tests.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Pre-knowledge Cutoff | | | Post-knowledge Cutoff | | |
|  | Highest | Lowest |  | Highest | Lowest |  |
|  | Quintile | Quintile | Difference | Quintile | Quintile | Difference |
| Goal-aware | 0.661%0.661\% | −0.891%-0.891\% | 1.552%∗⁣∗∗1.552\%^{\*\*\*} | 2.788%2.788\% | 0.518%0.518\% | 2.269%∗∗2.269\%^{\*\*} |
| Goal-blind | 0.095%0.095\% | −0.974%-0.974\% | 1.069%∗∗1.069\%^{\*\*} | 2.848%2.848\% | 0.609%0.609\% | 2.239%∗⁣∗∗2.239\%^{\*\*\*} |
| Difference |  |  | 0.483%∗∗0.483\%^{\*\*} |  |  | 0.030%0.030\% |

Table 2: Fama–MacBeth Regressions with Goal-Blind and Goal-Aware Sentiment Predictors



This table reports Fama and MacBeth ([1973](https://arxiv.org/html/2602.09504v1#bib.bib4 "Risk, return, and equilibrium: empirical tests")) coefficient estimates from monthly cross-sectional regressions of excess returns on sentiment measures derived from goal-blind and goal-aware GPT prompts. We estimate separate slopes for the pre– and post–knowledge cutoff periods by interacting each score with the corresponding indicator variable. “Diff" is defined as the goal-aware minus the goal-blind sentiment score. Column (1) controls stock betas estimated from past 60 months. Column (2) adds standard firm-level predictors (size and book-to-market). The bottom panel reports p-values for tests of equality between the pre- and post-cutoff coefficients for both the goal-blind score and the Diff measure. A positive and significant pre-cutoff Diff coefficient indicates that goal-aware scores contain incremental return-predictive information relative to goal-blind scores before the model’s knowledge cutoff.

|  | (1) | (2) |
| --- | --- | --- |
| Goal-Blind Score ×\times Pre-Cutoff | 1.279∗∗∗ | 1.281∗∗∗ |
|  | (0.394) | (0.387) |
| Goal-Blind Score ×\times Post-Cutoff | 1.273∗∗ | 1.283∗∗ |
|  | (0.505) | (0.474) |
| Diff ×\times Pre-Cutoff | 0.682∗∗ | 0.724∗∗ |
|  | (0.299) | (0.307) |
| Diff ×\times Post-Cutoff | -0.000 | 0.040 |
|  | (0.138) | (0.127) |
| Testing Coefficient Pre- and Post-Cutoff |  |  |
| Goal-blind Score: PP(Pre-Cutoff=Post-Cutoff) | 0.993 | 0.996 |
| Diff: PP(Pre-Cutoff=Post-Cutoff) | 0.046 | 0.048 |
| Control Predictors | Beta | Beta, Size, B/M ratio |
| NN | 16758 | 14863 |

  

Table 3: Regression Evidence on Differences in Out-of-Sample Predictive Performance Between Goal-Aware and Goal-Blind Sentiment Scores



This table reports regressions examining whether goal-aware sentiment scores deliver superior out-of-sample predictive performance relative to goal-blind scores in forecasting monthly stock returns. For each month, we estimate expanding-window forecasting models of excess returns using either the goal-aware or the goal-blind score measured at t−1t-1. We then compute out-of-sample accuracy using the conventional RO​O​S2R^{2}\_{OOS} measure, where the historical mean return serves as the benchmark forecast. We construct a 2×22\times 2 setting—pre- versus post–knowledge cutoff and goal-aware versus goal-blind predictions—and regress the resulting RO​O​S2R^{2}\_{OOS} values on indicators capturing how predictive performance changes after the knowledge cutoff for each score type. Although both prompts may embed correlations learned during model training, the differential shift between the two prompt types isolates the component of predictive performance attributable specifically to goal awareness—that is, GPT’s ability to adjust its scoring when informed that the output will be used for forecasting.

|  | (1) | (2) |
| --- | --- | --- |
| Goal-aware ×\times Post Cutoff | -0.058∗∗∗ | -0.059∗∗∗ |
|  | (0.008) | (0.008) |
| Controls | Yes | Yes |
| Firm FE | No | Yes |
| Time FE | Yes | Yes |
| Observations | 33497 | 33497 |
| R-squared | 0.007 | 0.038 |

  

* \*

  

Table 4: Fama–MacBeth Regressions with Goal-Blind and Goal-Aware Competition Threat Predictors



This table reports Fama–MacBeth (1973) estimates from quarterly cross-sectional regressions of earnings per share (EPS) on GPT-generated competition-threat scores. We separately estimate the return slopes for the pre– and post–knowledge cutoff periods by interacting each score with the corresponding indicator variable. Diff equals the difference between the goal-aware and goal-blind competition scores. Column (1) includes the predictors used in So (2013): EPS and a loss indicator. Column (2) adds all predictors from So (2013). The bottom panel reports pp-values testing whether the pre- and post-cutoff coefficients differ for both the goal-blind score and the Diff measure. A negative and significant pre-cutoff Diff coefficient indicates that the goal-aware competition score contains incremental information about next-quarter earnings relative to the goal-blind score before GPT’s knowledge cutoff. Post-cutoff coefficients assess whether this informational advantage persists when the model’s access to updated knowledge is truncated.

|  | (1) | (2) |
| --- | --- | --- |
| Goal-Blind Score ×\times Pre-Cutoff | -0.457∗∗∗ | -0.367∗∗ |
|  | (0.130) | (0.119) |
| Goal-Blind Score ×\times Post-Cutoff | -0.117 | -0.112∗ |
|  | (0.073) | (0.054) |
| Diff ×\times Pre-Cutoff | -0.188∗∗ | -0.178∗∗ |
|  | (0.081) | (0.072) |
| Diff ×\times Post-Cutoff | 0.056 | 0.044 |
|  | (0.091) | (0.073) |
| Testing Coefficient Pre- and Post-Cutoff |  |  |
| Goal-blind Score: PP(Pre-Cutoff=Post-Cutoff) | 0.083 | 0.132 |
| Diff: PP(Pre-Cutoff=Post-Cutoff) | 0.055 | 0.039 |
| Control Predictors | EPS, loss indicator in So ([2013](https://arxiv.org/html/2602.09504v1#bib.bib3 "A new approach to predicting analyst forecast errors: do investors overweight analyst forecasts?")) | All predictors in So ([2013](https://arxiv.org/html/2602.09504v1#bib.bib3 "A new approach to predicting analyst forecast errors: do investors overweight analyst forecasts?")) |
| NN | 5927 | 5918 |

  

Table 5: Regression Evidence on Differences in Out-of-Sample Predictive Performance Between Goal-Aware and Goal-Blind Competition Scores



This table reports regressions examining how the out-of-sample predictive performance of GPT-derived competition-threat scores changes after the model’s knowledge cutoff. For each quarter tt, we estimate expanding-window forecasting models of earnings growth, defined as E​P​StE​P​St−4\frac{EPS\_{t}}{EPS\_{t-4}}, using either the goal-blind or the goal-aware competition score measured at t−1t-1. For each firm–quarter observation, we compute out-of-sample accuracy using

RO​O​S2=1−yi,t^−yi,tyt−1¯−yi,tR^{2}\_{OOS}=1-\frac{\hat{y\_{i,t}}-y\_{i,t}}{\overline{y\_{t-1}}-y\_{i,t}}
yt−1¯\overline{y\_{t-1}} is the historical average of earnings growth and serves as the benchmark forecast. The dependent variable in all columns is this observation-level RO​O​S2R^{2}\_{OOS}. We regress the resulting RO​O​S2R^{2}\_{OOS} values on interactions between score type and the post-cutoff indicator. Negative coefficients indicate that predictive performance declines after the knowledge cutoff. Because both score types may embed correlations learned during training, the differential change between the goal-aware and goal-blind interactions isolates the incremental predictive content that arises specifically from goal-aware prompting—i.e., GPT’s ability to adjust its scoring when informed that the measure will be used for forecasting. A larger post-cutoff decline for the goal-aware scores implies that this task-aware component deteriorates more sharply once GPT’s access to updated information is truncated. Column (1) includes the baseline controls used in So (2013). Column (2) includes all predictors from So (2013) as well as firm fixed effects. pp-values for tests of equality across interaction terms are reported in the lower panel.

|  | (1) | (2) |
| --- | --- | --- |
| Goal-aware ×\times Post Cutoff | -5.370∗∗∗ | -5.370∗∗∗ |
|  | (1.177) | (1.177) |
| Controls | Yes | Yes |
| Firm FE | No | Yes |
| Time FE | Yes | Yes |
| Observations | 10860 | 10860 |
| R-squared | 0.023 | 0.147 |

## References

## References

* R. Bénabou and J. Tirole (2016)
  Mindful economics: the production, consumption, and value of beliefs.
  Journal of Economic Perspectives 30 (3),  pp. 141–164.
  Cited by: [footnote 1](https://arxiv.org/html/2602.09504v1#footnote1 "In 1 Introduction ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").
* S. Cao, C. C. Wang, and Y. Xiang (2025)
  When llm go abroad: foreign bias in ai financial predictions.
  Available at SSRN 5440116.
  Cited by: [§1](https://arxiv.org/html/2602.09504v1#S1.p7.1 "1 Introduction ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").
* J. Chen, G. Tang, G. Zhou, and W. Zhu (2025)
  ChatGPT and deepseek: can they predict the stock market and macroeconomy?.
  arXiv preprint arXiv:2502.10008.
  Cited by: [Appendix \thechapter.A](https://arxiv.org/html/2602.09504v1#X.A1.p4.1 "Appendix \thechapter.A Literature Review ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").
* L. D. Crane, A. Karra, and P. E. Soto (2025)
  Total recall? evaluating the macroeconomic knowledge of large language models.
  Cited by: [Appendix \thechapter.A](https://arxiv.org/html/2602.09504v1#X.A1.p2.1 "Appendix \thechapter.A Literature Review ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").
* E. F. Fama and J. D. MacBeth (1973)
  Risk, return, and equilibrium: empirical tests.
  Journal of political economy 81 (3),  pp. 607–636.
  Cited by: [§1](https://arxiv.org/html/2602.09504v1#S1.p5.1 "1 Introduction ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland."),
  [§2.3](https://arxiv.org/html/2602.09504v1#S2.SS3.p2.1 "2.3 Evaluation Metrics ‣ 2 Experimental Design and Data ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland."),
  [§2.3](https://arxiv.org/html/2602.09504v1#S2.SS3.p3.8 "2.3 Evaluation Metrics ‣ 2 Experimental Design and Data ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland."),
  [Table 2](https://arxiv.org/html/2602.09504v1#Sx2.T2 "In Tables ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").
* A. Fedyk, A. Kakhbod, P. Li, and U. Malmendier (2024)
  AI and perception biases in investments: an experimental study.
  Available at SSRN 4787249.
  Cited by: [§1](https://arxiv.org/html/2602.09504v1#S1.p7.1 "1 Introduction ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland."),
  [Appendix \thechapter.A](https://arxiv.org/html/2602.09504v1#X.A1.p6.1 "Appendix \thechapter.A Literature Review ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").
* P. Glasserman and C. Lin (2023)
  Assessing look-ahead bias in stock return predictions generated by gpt sentiment analysis.
  arXiv preprint arXiv:2309.17322.
  Cited by: [§1](https://arxiv.org/html/2602.09504v1#S1.p7.1 "1 Introduction ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland."),
  [Appendix \thechapter.A](https://arxiv.org/html/2602.09504v1#X.A1.p2.1 "Appendix \thechapter.A Literature Review ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").
* S. He, L. Lv, A. Manela, and J. Wu (2025)
  Chronologically consistent large language models.
  arXiv preprint arXiv:2502.21206.
  Cited by: [§1](https://arxiv.org/html/2602.09504v1#S1.p7.1 "1 Introduction ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland."),
  [Appendix \thechapter.A](https://arxiv.org/html/2602.09504v1#X.A1.p3.1 "Appendix \thechapter.A Literature Review ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").
* D. Hirshleifer, L. Peng, Q. Wang, W. Zhang, and X. Zhang (2025)
  Social finance in the age of ai: a tale of two platforms.
  Available at SSRN.
  Cited by: [§1](https://arxiv.org/html/2602.09504v1#S1.p7.1 "1 Introduction ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").
* M. Jha, J. Qian, M. Weber, and B. Yang (2024)
  Generative ai,managerial expectations, and economic activity.
  Available at SSRN 4976759.
  Cited by: [Appendix \thechapter.A](https://arxiv.org/html/2602.09504v1#X.A1.p4.1 "Appendix \thechapter.A Literature Review ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").
* H. Lee, J. Seo, S. Park, J. Lee, W. Ahn, C. Choi, A. Lopez-Lira, and Y. Lee (2025)
  Your ai, not your view: the bias of llms in investment analysis.
  In Proceedings of the 6th ACM International Conference on AI in Finance,
   pp. 150–158.
  Cited by: [Appendix \thechapter.A](https://arxiv.org/html/2602.09504v1#X.A1.p6.1 "Appendix \thechapter.A Literature Review ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").
* A. Lopez-Lira, Y. Tang, and M. Zhu (2025)
  The memorization problem: can we trust llms’ economic forecasts?.
  arXiv preprint arXiv:2504.14765.
  Cited by: [§1](https://arxiv.org/html/2602.09504v1#S1.p7.1 "1 Introduction ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland."),
  [Appendix \thechapter.A](https://arxiv.org/html/2602.09504v1#X.A1.p2.1 "Appendix \thechapter.A Literature Review ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").
* S. Mullainathan, J. Schwartzstein, and A. Shleifer (2008)
  Coarse thinking and persuasion.
  Quarterly Journal of Economics 123 (2),  pp. 577–619.
  Cited by: [footnote 1](https://arxiv.org/html/2602.09504v1#footnote1 "In 1 Introduction ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").
* S. Ouyang, H. Yun, and X. Zheng (2024)
  AI as decision-maker: risk preferences of llms.
  Available at SSRN 4851711.
  Cited by: [§1](https://arxiv.org/html/2602.09504v1#S1.p7.1 "1 Introduction ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").
* S. K. Sarkar and K. Vafa (2024)
  Lookahead bias in pretrained language models.
  Available at SSRN 4754678.
  Cited by: [§1](https://arxiv.org/html/2602.09504v1#S1.p7.1 "1 Introduction ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland."),
  [Appendix \thechapter.A](https://arxiv.org/html/2602.09504v1#X.A1.p2.1 "Appendix \thechapter.A Literature Review ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").
* K. Sharma, I. Dasgupta, B. Dhingra, L. Ouyang, and S. R. Bowman (2023)
  Towards understanding sycophancy in language models.
  arXiv preprint arXiv:2310.13548.
  Cited by: [§1](https://arxiv.org/html/2602.09504v1#S1.p9.1 "1 Introduction ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland."),
  [Appendix \thechapter.A](https://arxiv.org/html/2602.09504v1#X.A1.p5.1 "Appendix \thechapter.A Literature Review ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").
* J. Sheng, Z. Sun, B. Yang, and A. L. Zhang (2024)
  Generative ai and asset management.
  Available at SSRN 4786575.
  Cited by: [Appendix \thechapter.A](https://arxiv.org/html/2602.09504v1#X.A1.p4.1 "Appendix \thechapter.A Literature Review ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").
* E. C. So (2013)
  A new approach to predicting analyst forecast errors: do investors overweight analyst forecasts?.
  Journal of Financial Economics 108 (3),  pp. 615–640.
  Cited by: [Table 4](https://arxiv.org/html/2602.09504v1#Sx2.T4.13.19.6.2.1.1 "In Tables ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland."),
  [Table 4](https://arxiv.org/html/2602.09504v1#Sx2.T4.13.19.6.3.1.1 "In Tables ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").
* A. Tversky and D. Kahneman (1981)
  The framing of decisions and the psychology of choice.
  Science 211 (4481),  pp. 453–458.
  Cited by: [footnote 1](https://arxiv.org/html/2602.09504v1#footnote1 "In 1 Introduction ‣ Seeing the Goal, Missing the Truth: Human Accountability for AI Bias.We thank seminar participants at the University of Connecticut, the University of Maryland, Lancaster University, the University of California–Riverside, Singapore Management University, and NUS Business School for helpful feedback. Sean Cao gratefully acknowledges support from the Smith AI Initiative for Capital Markets Research at the University of Maryland.").

Appendix

## Appendix \thechapter.A Literature Review

This paper relates to a growing literature that evaluates the reliability of large language models (LLMs) in economic and financial applications. Existing research primarily attributes LLM bias or overperformance to unintended training data access and distortions in exploration strategies and model weights. Our study differs in focus and mechanism. We show that even when inputs, models, and scoring tasks are held fixed, human disclosure of downstream objectives at inference time can systematically distort intermediate LLM outputs. The resulting bias arises from prompt framing rather than from training data or model architecture.

One strand of research shows that LLM predictions may reflect memorization or look-ahead bias from pretraining data. Studies such as Lopez-Lira et al. ([2025](https://arxiv.org/html/2602.09504v1#bib.bib9 "The memorization problem: can we trust llms’ economic forecasts?")), Sarkar and Vafa ([2024](https://arxiv.org/html/2602.09504v1#bib.bib1 "Lookahead bias in pretrained language models")), and Glasserman and Lin ([2023](https://arxiv.org/html/2602.09504v1#bib.bib8 "Assessing look-ahead bias in stock return predictions generated by gpt sentiment analysis")) document that LLM forecasts and sentiment measures can embed future information relative to the intended evaluation window, even when prompts attempt to enforce historical information sets. Related work shows that anonymizing or masking firm identifiers can change model outputs, indicating that stored contextual knowledge can affect measurement tasks (Crane et al., [2025](https://arxiv.org/html/2602.09504v1#bib.bib6 "Total recall? evaluating the macroeconomic knowledge of large language models")). These papers focus on leakage from training data into inference. Our design instead keeps the information set constant and varies only whether downstream use is disclosed. The performance difference we estimate is thus tied to objective disclosure rather than to temporal leakage.

A separate line of work proposes chronologically constrained model construction as a solution. For example, He et al. ([2025](https://arxiv.org/html/2602.09504v1#bib.bib7 "Chronologically consistent large language models")) develop language models trained only on text available up to each date and show that such models perform competitively in asset pricing tasks. This approach addresses bias at the training stage. Our results are complementary: even with a fixed model and a known knowledge cutoff, output distortions can arise from inference-time prompt design alone. Training-stage controls do not remove bias if downstream goals are revealed during deployment.

An emerging literature uses LLMs as tools for measurement and signal extraction from text. Studies such as Jha et al. ([2024](https://arxiv.org/html/2602.09504v1#bib.bib13 "Generative ai,managerial expectations, and economic activity")), Chen et al. ([2025](https://arxiv.org/html/2602.09504v1#bib.bib15 "ChatGPT and deepseek: can they predict the stock market and macroeconomy?")), and Sheng et al. ([2024](https://arxiv.org/html/2602.09504v1#bib.bib5 "Generative ai and asset management")) show that LLM-derived measures of expectations, sentiment, and news content can predict macroeconomic outcomes and asset returns. Our study is close in design because we also use LLM outputs as intermediate variables in standard forecasting regressions. The difference is that most prior work treats these constructed measures as stable or neutral conditional on the input text and prompt instructions. Instead, we show that they are sensitive to whether the downstream predictive use is disclosed. The same text and model can produce systematically different intermediate measures when the evaluation objective is stated.

In addition, our results relate to the computer science literature on a specific aspect of alignment failure in the form of reward hacking, specification gaming, and sycophancy (Sharma et al., [2023](https://arxiv.org/html/2602.09504v1#bib.bib23 "Towards understanding sycophancy in language models")). In those settings, models adjust outputs toward signals of user approval or reward rather than task correctness. We document a related mechanism in an economic measurement setting. When informed of an evaluation objective, an LLM shifts intermediate outputs toward patterns associated with that objective. In our design there is no change in rewards, parameters, or fine tuning. The distortion is induced by prompt-level disclosure of purpose.444In computer science terms, this mechanism is related to objective misgeneralization and proxy optimization, where a model conditions on inferred evaluation criteria rather than only on the stated task. Our setting shows that this behavior can arise from prompt framing alone, without retraining or reinforcement signals.

Finally, our paper connects to work on AI-induced biases in financial and investment contexts, including representational and preference-driven distortions in model outputs (Fedyk et al., [2024](https://arxiv.org/html/2602.09504v1#bib.bib24 "AI and perception biases in investments: an experimental study"); Lee et al., [2025](https://arxiv.org/html/2602.09504v1#bib.bib26 "Your ai, not your view: the bias of llms in investment analysis")). That literature studies biases linked to identities, beliefs, or investor types reflected in training data. We identify a different channel: Goal-conditioned distortion that arises from downstream-use disclosure even when the task is purely technical and the inputs are unchanged.

Taken together, existing studies emphasize the informational (data-side) and structural (model-side) sources of bias. Our study introduces a user-side source that operates through downstream-objective disclosure at inference. We provide a design that isolates this effect on intermediate LLM-generated measures within financial prediction.

## Appendix \thechapter.B Prompts

### Goal-blind

> "For the following tasks, all dates are expressed in the format MM/DD/YYYY (month/day/year).
>   
> Below is the earnings call transcript of {ticker}. Please provide a continuous sentiment score in [-1, 1] about the firm’s business sentiment for the month ending on {date}.
>   
> Provide a precise numerical answer. Format as a JSON object with the following fields:
>   
> - answer: The precise numerical answer to the question. No strings.
>   
> {the firm’s earnings call transcript}."

### Goal-aware

> "For the following tasks, all dates are expressed in the format MM/DD/YYYY (month/day/year).
>   
> Below is the earnings call transcript of {ticker}. Please provide a continuous sentiment score in [-1, 1] about the firm’s business sentiment for the month ending on {date}. The sentiment score later will be used as an explanatory variable in a regression to predict the monthly stock returns ending on {date}.
>   
> Provide a precise numerical answer. Format as a JSON object with the following fields:
>   
> - answer: The precise numerical answer to the question. No strings.
>   
> {the firm’s earnings call transcript}."