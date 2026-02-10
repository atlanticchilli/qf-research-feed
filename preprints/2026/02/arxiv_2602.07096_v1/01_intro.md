---
authors:
- Yuyang Dai
- Yan Lin
- Zhuohan Xie
- Yuxia Wang
doc_id: arxiv:2602.07096v1
family_id: arxiv:2602.07096
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'RealFin: How Well Do LLMs Reason About Finance When Users Leave Things Unsaid?'
url_abs: http://arxiv.org/abs/2602.07096v1
url_html: https://arxiv.org/html/2602.07096v1
venue: arXiv q-fin
version: 1
year: 2026
---

prompt = f"Instruction: {system_prompt}\n
Input: {user_prompt}\n
Answer: "
```



Figure 10: FinGPT-Falcon-7B inference template for English CFA tasks.



|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Benchmark Subset | Total | Answer Acc. | Reasoning Acc. | Mean Conf. |
| Revised English CFA (Masked) | 367 | 3.5% | 0.0% | 50.3 |

Table 19: FinGPT-7B performance on NOTA masked questions.

#### Detailed Results.

As shown in Tables [20](https://arxiv.org/html/2602.07096v1#A3.T20 "Table 20 ‣ Detailed Results. ‣ C.9 FinGPT Configuration ‣ Appendix C LLMs Implementation Details ‣ RealFin: How Well Do LLMs Reason About Finance When Users Leave Things Unsaid?") and [20](https://arxiv.org/html/2602.07096v1#A3.T20 "Table 20 ‣ Detailed Results. ‣ C.9 FinGPT Configuration ‣ Appendix C LLMs Implementation Details ‣ RealFin: How Well Do LLMs Reason About Finance When Users Leave Things Unsaid?"), FinGPT-7B achieved an overall accuracy of only 2.19% (Original) and 3.54% (Revised), significantly below random guessing. Qualitative inspection revealed that the model frequently outputs sentiment markers (e.g., “positive/negative”) or jumbled characters instead of logical steps. This confirms that its fine-tuning distribution—highly specialized for sentiment classification—severely compromises its capacity for multi-step financial deduction.

(a) Accuracy (%) by Topic

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Topic | Orig. | Rev. | Δ\Delta | n |
| Corp. Fin. | 0.00 | 0.00 | 0.00 | 10 |
| Derivatives | 6.67 | 4.00 | –2.67 | 45 |
| Economics | 0.00 | 0.00 | 0.00 | 15 |
| Equity | 1.69 | 3.85 | +2.16 | 59 |
| FSA | 2.33 | 3.70 | +1.37 | 43 |
| Fixed Inc. | 0.00 | 0.00 | 0.00 | 49 |
| Other Inv. | 3.19 | 3.70 | +0.51 | 94 |
| Portfolio | 0.00 | 33.33 | +33.33 | 4 |
| Quant. | 0.00 | 2.22 | +2.22 | 47 |
| Overall | 2.19 | 3.54 | +1.35 | 366 |

(b) Accuracy (%) by Question Type

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Question Type | Orig. | Rev. | Δ\Delta | n |
| Conceptual | 1.61 | 6.98 | +5.37 | 62 |
| Simple Calc. | 6.67 | 2.79 | –3.88 | 30 |
| Complex Calc. | 0.00 | 0.00 | 0.00 | 15 |
| Comp. Judgment | 1.98 | 4.65 | +2.67 | 101 |
| Know. App. | 0.00 | 0.00 | 0.00 | 86 |
| Stat. Methods | 4.29 | 2.13 | –2.16 | 70 |
| Overall | 2.19 | 3.54 | +1.35 | 364 |

Table 20: Performance of FinGPT-7B on English CFA Benchmark.

#### Robustness Analysis under Adversarial Masking.

FinGPT-7B undergoes a total functional collapse in NOTA-masked scenarios (Table [19](https://arxiv.org/html/2602.07096v1#A3.T19 "Table 19 ‣ Chat Template. ‣ C.9 FinGPT Configuration ‣ Appendix C LLMs Implementation Details ‣ RealFin: How Well Do LLMs Reason About Finance When Users Leave Things Unsaid?")). The near-zero reasoning accuracy and stagnant confidence score (∼\sim50.0) reveal an absolute lack of logical plasticity. Rather than identifying missing information, the model reverts to fixed templates, proving that sentiment-optimized models remain inherently fragile in adversarial professional environments.

General Models
Financial Models


GPT-5.1-m
Gem-2.5
Cl-3.5
DS-V3
Qwen3
XY-70B
Fin-R1
DJ-32B
FL-8B
FQ-7B
CFGPT2
DISC

Question Type
O
R
O
R
O
R
O
R
O
R
O
R
O
R
O
R
O
R
O
R
O
R
O
R

English CFA

Conceptual
82.14
90.12
80.23
89.45
79.87
91.23
75.12
87.98
80.45
90.56
77.42
79.07
69.35
76.74
80.65
86.05
40.32
60.47
51.61
67.44
56.45
76.74
8.06
18.60

Simple Calc.
78.56
87.23
77.89
86.12
76.34
88.76
72.45
85.34
77.23
87.89
36.67
82.12
50.00
82.12
66.67
87.15
23.33
53.63
36.67
62.57
30.00
68.16
23.33
20.67

Complex Calc.
75.23
86.45
74.12
85.78
73.89
87.12
70.67
84.23
74.56
86.34
33.33
100.00
26.67
100.00
60.00
100.00
13.33
75.00
26.67
100.00
40.00
100.00
6.67
25.00

Comp. Judg.
81.45
89.78
79.67
88.23
78.23
90.12
74.56
86.89
79.12
89.45
62.38
88.37
57.43
84.88
84.16
89.53
41.58
62.79
43.56
61.63
60.40
80.23
22.77
22.09

Knowledge App.
79.87
88.45
78.12
87.12
77.56
89.34
73.23
85.67
78.45
88.78
40.70
75.00
38.37
75.00
44.19
87.50
24.42
62.50
19.77
50.00
31.40
75.00
10.47
12.50

Stats Methods
83.45
91.67
81.23
90.12
80.56
92.34
76.89
88.45
81.67
91.23
71.43
93.62
61.43
93.62
90.00
91.49
35.71
57.45
44.29
80.85
48.57
76.60
2.86
14.89

All
80.59
89.01
78.99
88.19
77.81
89.62
73.55
86.34
78.42
88.83
58.47
84.74
54.10
83.65
72.95
88.28
33.61
57.49
38.52
65.40
47.54
73.57
13.11
19.89

Chinese CPA

Conceptual
82.34
69.12
75.23
86.45
71.12
82.34
82.89
81.67
78.12
93.89
10.92
80.00
7.56
90.00
15.13
90.00
9.24
40.00
8.40
30.00
2.52
40.00
4.20
30.00

Simple Calc.
80.67
67.89
73.45
84.12
69.34
80.12
81.23
79.89
76.45
91.23
9.76
64.15
7.32
71.70
4.88
62.26
4.88
30.19
9.76
18.87
4.88
49.06
4.88
15.09

Complex Calc.
79.23
66.45
72.12
82.78
68.12
78.89
80.45
78.23
75.23
89.67
0.00
–
0.00
–
0.00
–
0.00
–
0.00
–
0.00
–
0.00
–

Comp. Judg.
81.45
68.56
74.23
85.12
70.23
81.23
81.89
80.56
77.12
92.45
10.34
71.72
5.75
72.73
13.79
84.85
8.05
25.25
4.60
34.34
2.30
49.49
5.75
20.20

Knowledge App.
80.12
67.23
73.12
83.45
69.12
79.67
81.12
79.12
76.23
90.89
0.00
66.67
14.29
66.67
0.00
100.00
0.00
33.33
14.29
33.33
0.00
0.00
14.29
0.00

Stats Methods
82.67
69.89
75.67
86.89
71.45
82.89
83.12
82.12
78.56
94.23
16.67
60.00
10.42
70.00
20.83
70.00
8.33
30.00
6.25
20.00
4.17
80.00
2.08
30.00

All
80.81
68.45
73.42
84.80
69.37
80.46
81.06
80.00
76.32
92.00
11.18
69.14
7.57
73.14
13.82
77.71
7.89
28.00
7.24
28.57
2.96
49.71
4.61
19.43

Table 21: Accuracy (%) across six question types for English CFA (top) and Chinese CPA (bottom). O = original; R = revised. For each row: Best-O, Best-R, Worst-O, Worst-R; best per row is bolded. DJ-32B = DianJin-R1-32B; FL-8B = Finance-Llama-8B; FQ-7B = Finance-Qwen-7B.



General Models
Financial Models


GPT-5.1-m
Gem-2.5
Cl-3.5
DS-V3
Qwen3
XY-70B
Fin-R1
DJ-32B
FL-8B
FQ-7B
CFGPT2
DISC

Topic
O
R
O
R
O
R
O
R
O
R
O
R
O
R
O
R
O
R
O
R
O
R
O
R

English CFA

Corp. Finance
82.50
90.00
91.25
100.00
81.88
90.00
82.19
90.00
83.75
91.00
60.00
90.00
50.00
90.00
80.00
90.00
60.00
90.00
40.00
70.00
60.00
90.00
30.00
40.00

Derivatives
80.00
88.00
87.20
96.00
83.68
92.00
80.08
88.00
82.80
90.00
53.33
92.00
53.33
88.00
62.22
96.00
28.89
64.00
28.89
68.00
31.11
76.00
20.00
28.00

Economics
81.82
90.00
81.82
90.00
81.82
90.00
81.82
90.00
81.82
89.09
53.33
80.00
53.33
60.00
60.00
90.00
13.33
40.00
46.67
80.00
53.33
60.00
13.33
0.00

Equity Inv.
79.49
88.46
79.49
88.46
79.49
88.46
76.28
84.62
78.85
87.18
57.63
86.54
62.71
86.54
76.27
88.46
37.29
53.85
40.68
67.31
59.32
78.85
20.34
13.46

FSA
79.66
88.89
79.66
88.89
79.66
88.89
79.66
88.89
79.66
89.63
65.12
88.89
39.53
81.48
76.74
88.89
34.88
48.15
41.86
48.15
53.49
66.67
11.63
22.22

Fixed Income
71.43
78.57
71.43
78.57
71.43
78.57
71.43
78.57
71.43
76.79
42.86
78.57
32.65
85.71
46.94
78.57
18.37
50.00
24.49
57.14
36.73
57.14
14.29
14.29

Other Inv.
79.75
88.89
77.78
86.42
79.75
88.89
76.54
85.19
78.02
86.42
62.77
86.42
57.45
87.65
79.79
88.89
41.49
69.14
36.17
71.60
50.00
77.78
10.64
23.46

Portfolio Mgt
90.91
100.00
90.91
100.00
90.91
100.00
90.91
100.00
90.91
100.00
75.00
100.00
75.00
100.00
100.00
100.00
50.00
100.00
50.00
100.00
75.00
100.00
0.00
33.33

Quant Analysis
80.00
88.89
80.00
88.89
82.09
91.11
78.21
86.67
78.61
87.78
65.96
86.67
72.34
88.89
89.36
88.89
31.91
64.44
57.45
82.22
42.55
73.33
0.00
6.67

All
80.59
89.01
78.99
88.19
77.81
89.62
73.55
86.34
78.42
88.83
58.47
84.74
54.10
83.65
72.95
88.28
33.61
57.49
38.52
65.40
47.54
73.57
13.11
19.89

Chinese CPA

Accounting
33.33
36.67
75.76
83.33
72.73
80.00
66.67
73.33
69.32
85.00
4.49
63.33
6.74
66.67
7.87
60.00
7.87
33.33
7.87
20.00
2.25
60.00
4.49
26.67

Auditing
84.85
93.33
90.91
100.00
87.88
96.67
84.85
93.33
88.64
97.50
25.76
96.67
13.64
83.33
36.36
93.33
4.55
33.33
4.55
60.00
7.58
60.00
4.55
26.67

Economic Law
66.28
72.97
78.57
86.49
76.19
83.78
81.08
89.19
73.81
90.63
6.67
78.38
6.67
91.89
8.33
89.19
11.67
21.62
8.33
13.51
1.67
45.95
6.67
18.92

Tax Law
67.11
73.81
75.76
83.33
69.23
76.19
80.10
88.10
71.43
85.94
15.79
66.67
7.02
71.43
8.77
88.10
10.53
14.29
8.77
23.81
1.75
40.48
5.26
14.29

Wealth Mgt.
45.45
50.00
58.06
63.89
60.61
66.67
50.51
55.56
54.55
67.50
0.00
44.44
0.00
52.78
3.12
55.56
3.12
41.67
6.25
30.56
0.00
47.22
0.00
13.89

All
80.81
68.45
73.42
84.80
69.37
80.46
81.06
80.00
76.32
92.00
11.18
69.14
7.57
73.14
13.82
77.71
7.89
28.00
7.24
28.57
2.96
49.71
4.61
19.43

Table 22: Accuracy (%) across financial topics for English CFA (top) and Chinese CPA (bottom). O = original; R = revised. For each row: Best-O, Best-R, Worst-O, Worst-R; best per row is bolded. DJ-32B = DianJin-R1-32B; FL-8B = Finance-Llama-8B; FQ-7B = Finance-Qwen-7B.



|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| General Models | | | | Financial Models | | | |
| Model | Chinese | English | Average | Model | Chinese | English | Average |
| Gemini 2.5 Flash | 48.78 | 72.38 | 60.58 | Fin-R1-7B | 77.10 | 84.50 | 81.10 |
| Claude 3.5 Sonnet | 37.36 | 70.11 | 53.73 | XuanYuan3-70B | 61.70 | 84.70 | 73.20 |
| Qwen3-Max | 44.85 | 59.94 | 52.39 | DianJin-R1-32B | 77.71 | 88.28 | 83.00 |
| GPT-5.1-mini | 30.64 | 68.23 | 49.44 | FL-8B | 28.57 | 56.95 | 42.76 |
| DeepSeek V3 | 36.21 | 56.87 | 46.54 | FQ-7B | 48.00 | 62.67 | 55.34 |
|  |  |  |  | CFGPT2-7B | 54.90 | 75.20 | 65.05 |
|  |  |  |  | DISC-FinLLM-13B | 20.00 | 12.26 | 16.13 |
| Avg. | 39.57 | 65.51 | 52.54 | Avg. | 52.57 | 66.37 | 59.51 |

Table 23: Cross-comparison of model accuracy (%) on None of The Above questions compared to Revised accuracy. Green indicates NOTA accuracy higher than Revised; red indicates lower; gray indicates NOTA equals Revised. FL-8B = Finance-Llama-8B; FQ-7B = WiroAI Finance-Qwen-7B.