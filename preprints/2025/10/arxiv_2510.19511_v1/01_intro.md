---
authors:
- Jan Dhaene
- Atibhav Chaudhry
- Ka Chun Cheung
- Austin Riis-Due
doc_id: arxiv:2510.19511v1
family_id: arxiv:2510.19511
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Compensation-based risk-sharing
url_abs: http://arxiv.org/abs/2510.19511v1
url_html: https://arxiv.org/html/2510.19511v1
venue: arXiv q-fin
version: 1
year: 2025
---


Jan Dhaene
jan.dhaene@kuleuven.be, KU Leuven, Belgium
  
Atibhav Chaudhry
atibhav.chaudhry@kuleuven.be, University of Melbourne, Australia and KU Leuven, Belgium
  
Ka Chun Cheung
kccg@hku.hk, University of Hong Kong, Hong Kong
  
Austin Riis-Due
austincarter.riis-due@uwaterloo.ca, University of Waterloo, Canada

###### Abstract

This paper studies the mathematical problem of allocating payouts (compensations) in an endowment contingency fund using a risk-sharing rule that satisfies full allocation. Besides the participants, an administrator manages the fund by collecting ex-ante contributions to establish the fund and distributing ex-post payouts to members. Two types of administrators are considered. An ‘active’ administrator both invests in the fund and receives the payout of the fund when no participant receives a payout. A ‘passive’ administrator performs only administrative tasks and neither invests in nor receives a payout from the fund. We analyze the actuarial fairness of both compensation-based risk-sharing schemes and provide general conditions under which fairness is achieved. The results extend earlier work by Denuit and Robert (2025) and Dhaene and Milevsky (2024), who focused on payouts based on Bernoulli distributions, by allowing for general non-negative loss distributions.

#### Keywords:

decentralized insurance; centralized insurance; P2P insurance; compensation-based risk-sharing; contribution-based risk-sharing; tontines.

## 1 Centralized vs. decentralized risk-pooling

Consider a group of nn individuals observed at time 0, each of them exposed
to a non-negative random loss at time 11. This loss can be related to a
well-defined peril (e.g., hospitalization-related or critical illness-related
expenses), or it can be expressed as a deterministic claim payment contingent
on the occurrence of a well-defined event (e.g., a deterministic payment
contingent on death or survival).

In the classical insurance approach, individuals involve an
insurer and each of them buys an insurance contract at time 0, which
entitles them to their respective observed losses at time 11. Every
policyholder is compensated ex-post (at time 11) for his experienced loss.
In return for this coverage, the insurer charges each policyholder an ex-ante insurance premium (at time 0). In such an insurance coverage, the aggregate risk
(randomness) of the insurance portfolio is taken over by the insurer. This
risk transfer is possible if the pool consists of a sufficient number of
mutually independent and homogeneous risks, with premiums being calculated in
a conservative way. In addition, the insurer sets up solvency capital for the
case that the collected premiums turn out to be insufficient to cover the
guaranteed claims. Premiums and solvency capital are chosen so that the
probability of the event that the sum of all accumulated premiums and solvency
capital exceeds the aggregate claims of the insurance portfolio is
sufficiently large (e.g., 99.5%). Classical insurance as described above is a
form of centralized risk transfer, meaning that it is a risk-transfer
mechanism in which individual losses faced by policyholders are transferred
to a central insurer who guarantees that losses will be paid. In exchange, policyholders pay a risk premium and compensate the insurer’s shareholders by providing a return on the capital they set aside to maintain the insurer’s guarantee.

Instead of a transfer of the aggregate risk of the pool to a central insurer
(guarantor), individuals can opt for a so-called decentralized
risk-sharing approach, where individuals do not transfer the aggregate losses
to a guarantor but keep the aggregate risk within the pool, without
generating or creating any solvency risk. Examples of such approaches can be found in Abdikerimova and Feng (2022) and the references
therein. One way to achieve this
goal is that the premiums at time 0 of the classical centralized approach are
replaced by time 11 contributions: Each participant in the risk-sharing pool
is fully compensated for his loss at time 11, but in return he pays a
contribution to the pool at time 11. These contributions are time 11 measurable random
variables, chosen at time 0. The risk-sharing scheme is set up
such that the sum of all contributions paid at time 11 by the participants is
exactly equal to the sum of all losses covered by the pool. This constraint
is called the full allocation condition. In other words, participants
contribute at time 11, by sharing total losses once they have
been observed. Following Dhaene and Milevsky (2024), we call such a
decentralized approach contribution-based risk-sharing.

A simple example of such a risk-sharing approach is the uniform risk-sharing
rule, where each participant’s contribution is set equal to the observed
aggregate losses of the pool, divided by the number of participants. Other
examples of contribution-based risk-sharing are the conditional-mean risk
sharing scheme, introduced in the actuarial literature in Denuit and Dhaene
(2012), and the quantile risk-sharing scheme introduced in Denuit, Dhaene and
Robert (2022). The properties of contribution-based
risk-sharing rules have been investigated in detail in Denuit, Dhaene and
Robert (2022) and Denuit, Dhaene, Ghossoub and Robert (2025), among others. An
axiomatic characterization of the conditional mean risk-sharing rule is given
in Jiao, Kou, Liu and Wang (2023), while an axiomatic characterization of the
quantile risk-sharing rule is considered in Dhaene, Cheung, Robert and Denuit
(2025). Axiomatic characterizations of some simple risk-sharing rules,
including the uniform rule, are presented in Dhaene, Kazzi and Valdez (2025).

Decentralized risk-sharing can also be constructed in another way. Indeed,
suppose again that all participants are exposed to a random non-negative loss at time 11. Each of them invests an amount at time 0 to set up a so-called ‘endowment
contingency fund’. At time 11, the total fund value
is shared among all participants. The relative part that each participant will
receive is a time 11 observable random variable, determined at time 0 as a
well-defined function of the claims and eventually also of other
information that will be observable at time 11. Solvency is guaranteed by the full allocation condition which states
that the sum of all payments to the participants at time 11 is equal to the fund
value at time 11. The aim of an ‘endowment contingency fund’ is to provide
participants with a cheaper and effective protection, compared to commercial
insurance. The term ‘endowment’ indicates that it is an investment portfolio
with initial capital deriving from cash inflows, whereas the term
‘contingency’ means that the payments out of this fund are contingent on the
realization of certain random events. For each individual participant, the
coverage ratio (i.e., compensation over claim) depends on the initial
investments and the observed losses of all participants. A participant may
not receive his observed loss, i.e., he might not be fully compensated for his
loss, or even receive more than his loss. In this setting, the time 11
payments can be considered as a kind of compensation for the occurred
losses. Therefore, Dhaene and Milevsky (2024) call the time 11 payments from
the fund to the participants the compensations, and they baptize this
decentralized risk-sharing approach compensation-based risk-sharing.

As a simple example of the compensation-based approach, consider the
risk-sharing scheme where at time 11, each
participant receives a compensation which is proportional to his observed
loss. The proportionality factor, which is observable at time 11, is assumed to be equal for all participants and follows
from the full allocation condition.

Special cases of compensation-based risk-sharing schemes have been
investigated in several actuarial papers, including Denuit and Robert (2025), Dhaene and Milevsky (2024) and Bernard, Feliciangeli and Vanduffel (2025), where only two-point distributed losses (indicator random variables) have
been considered. In the current paper, we generalize the approach set up in these papers to include general losses and further explore properties of general compensation-based risk-sharing schemes. Our generalization broadens the applicability of such schemes to a wider range of insurance types with random claim severity, for example, homeowners and automobile insurance. We analyze the role of an administrator in such schemes and compare frameworks with an active and a passive administrator.

All random variables considered in this paper are defined on the probability space (Ω,ℱ,ℙ)\left(\Omega,\mathcal{F},\mathbb{P}\right). The set of all non-negative random variables on (Ω,ℱ,ℙ)\left(\Omega,\mathcal{F},\mathbb{P}\right) is denoted by L+0L\_{+}^{0}. Throughout
this paper, the term ‘positive’ is used for ‘strictly larger than zero’. The
set of non-negative real numbers is denoted by ℝ+\mathbb{R}^{+}.

## 2 Compensation-based risk-sharing with an active administrator

In this paper, we introduce and investigate a general type of fully-funded
risk-sharing (further abbreviated as RS) mechanisms, where nn participants
decide to mutually invest and set up a so-called ‘contingency endowment
fund’. At the beginning of the investment period, each participant ii makes
an initial (non-negative) investment πi\pi\_{i} in the fund (similar to paying
an initial insurance premium). Throughout this paper, we always implicitly
assume that at least one of these investments is positive, which means that
for at least one participant ii, i=1,2,…,ni=1,2,\ldots,n, one has that πi>0\pi\_{i}>0.
The beginning of the investment period is denoted by time 0, and also
referred to as ‘now’. The end of the investment period is denoted by time 11, also referred to as ‘the end of the year’. In practice, these investments will be supplemented with fees to cover expenses, but we assume that the investments πi\pi\_{i} are net investments, after fees for expenses have been paid. In this case, we do not further have to take these fees into account in our analysis.

Our objective is to investigate fair methods for the participants to divide
the total initial investment among themselves at time 11. To be more precise, at time 0,
the time 11 observable non-negative random variables WiW\_{i} are chosen, where WiW\_{i}
stands for the part of the total fund value available at time 11 that will be
attributed to the participant ii at this time. Following Dhaene and Milevsky
(2024), we call these amounts to be paid at time 11 the ‘compensations’ to the
participants. In general, there is the possibility that the time 11
realizations of all compensations WiW\_{i}, i=1,2,…,ni=1,2,\ldots,n, are equal to 0.
At time 0, we have to clearly specify what happens to the fund’s proceeds in
this case.

Apart from the nn participants, there is another agent, denoted by n+1n+1 and
called the administrator. The role of the administrator is to collect the amounts πi\pi\_{i} at
time 0, to invest them, and to distribute the compensations WiW\_{i} to the
nn participants at time 11. Seen from time 0, the compensations to the nn participants are random variables defined and agreed upon by the participants at that time. As mentioned above, it might happen that all
compensations to the participants are equal to 0. We assume that in case
this situation occurs, the administrator receives the full proceeds of the
fund. On the other hand, in case the time 11 realization of the compensation
of at least one participant is positive, the administrator does not receive
anything. The administrator’s compensation at time 11 is denoted by
Wn+1W\_{n+1}. We assume that the administrator also contributes an initial
(non-negative) investment πn+1\pi\_{n+1} to the fund, in return of receiving the
total proceeds of the fund when Wi=0,W\_{i}=0, i=1,2,…,ni=1,2,\ldots,n.

When referring to the ‘n+1n+1 agents’ of a compensation-based RS scheme, we
mean the nn participants and the administrator. The sum of the initial
investments of all agents, that is, ∑j=1n+1πj\sum\_{j=1}^{n+1}\pi\_{j}, is equal to the total
value of the fund at the beginning of the investment period. For simplicity,
we assume a zero interest rate and no expenses, but our results can easily be generalized to
the case of a (deterministic) investment return and expenses by assuming ∑j=1n+1πj\sum\_{j=1}^{n+1}\pi\_{j} is the accumulated value of the investments net of expenses. Under this assumption, the
time 11 value of the investment fund is equal to ∑j=1n+1πj\sum\_{j=1}^{n+1}\pi\_{j}.
Notice that our implicit assumption that at least one of the participants’
investments is positive implies that the time 11 value of the fund is always positive.

The active administrator’s time 11 claim Wn+1W\_{n+1} on the fund can be
expressed as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wn+1={∑j=1n+1πj:W1=W2=⋯=Wn=00: otherwise W\_{n+1}=\left\{\begin{array}[c]{ll}\sum\_{j=1}^{n+1}\pi\_{j}&:W\_{1}=W\_{2}=\cdots=W\_{n}=0\\ 0&:\text{ otherwise \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }\end{array}\right. |  | (1) |

This means that the administrator receives the full proceeds of the fund if
and only if all other participants receive zero compensation. Taking into
account that all compensations are non-negative, the event
W1′=W2=…=Wn=0′{}^{\prime}W\_{1}=W\_{2}=\ldots=W\_{n}=0^{\prime} is equivalent to the event
∑j=1n′Wj=0′{}^{\prime}\sum\_{j=1}^{n}W\_{j}=0^{\prime}. The random variables ∑j=1nWj\sum\_{j=1}^{n}W\_{j}
and Wn+1W\_{n+1} exhibit a dependency structure which is a special case of
‘countermonotonicity’, called ‘mutual exclusivity’, meaning that both random variables
are non-negative, with one of them being positive implying that the other one
is equal to 0. The concept of ‘mutual exclusivity’ is considered in several
papers in the actuarial literature, see for example, Dhaene and Denuit (1999), Cheung
and Lo (2014) and Lauzier, Lin and Wang (2024).

Introducing the random variable Pn+1P\_{n+1}, with 0≤Pn+1≤10\leq P\_{n+1}\leq 1, for the proportion
of the aggregate investment that will be attributed to the administrator,
the compensation Wn+1W\_{n+1} can be expressed as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wn+1=(∑j=1n+1πj)×Pn+1,W\_{n+1}=\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times P\_{n+1}, |  | (2) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pn+1={1:W1=W2=⋯=Wn=00:otherwise P\_{n+1}=\left\{\begin{array}[c]{ll}1&:W\_{1}=W\_{2}=\cdots=W\_{n}=0\\ 0&:\text{otherwise \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }\end{array}\right. |  | (3) |

Introducing the random variable PiP\_{i}, with 0≤0\leq Pi≤1P\_{i}\leq 1, for the random
proportion of the aggregate investment attributed to participant ii, we have
that the compensations of the participants can be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wi=(∑j=1n+1πj)×Pii=1,2,…,n.W\_{i}=\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times P\_{i}\qquad i=1,2,\ldots,n. |  | (4) |

Taking into account ([4](https://arxiv.org/html/2510.19511v1#S2.E4 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), the random relative compensation Pn+1P\_{n+1} attributed to
the administrator can be expressed as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pn+1={1:P1=P2=⋯=Pn=00:otherwise, P\_{n+1}=\left\{\begin{array}[c]{ll}1&:P\_{1}=P\_{2}=\cdots=P\_{n}=0\\ 0&:\text{otherwise, \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }\end{array}\right. |  | (5) |

or equivalently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pn+1=1​(∑j=1nPj=0),P\_{n+1}={1}\left(\sum\_{j=1}^{n}P\_{j}=0\right), |  | (6) |

where 1​(A){1}\left(A\right) stands for the indicator function, which
is 11 if the event AA occurs and 0 otherwise. This expression for Pn+1P\_{n+1} also shows that ∑j=1nPj\sum\_{j=1}^{n}P\_{j} and Pn+1P\_{n+1} are mutually exclusive.

Hereafter, we always assume that at time 11, the total amount of the
available funds is fully distributed to the participants and the
administrator, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑j=1n+1Pj=1.\sum\_{j=1}^{n+1}P\_{j}=1. |  | (7) |

This condition is called the full allocation condition for the
compensation-based RS scheme. We also always implicitly assume that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0<Pr⁡[Pn+1=0]<1,0<\Pr\left[P\_{n+1}=0\right]<1, |  | (8) |

or equivalently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0<Pr⁡[Pn+1=1]<1.0<\Pr\left[P\_{n+1}=1\right]<1. |  | (9) |

The assumption ([8](https://arxiv.org/html/2510.19511v1#S2.E8 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) means that the events ‘at least one participant
receives a non-zero compensation’ and ‘all participants receive a
zero-compensation’ have a positive probability. Taking into account that
Pn+1P\_{n+1} is Bernoulli distributed, from ([9](https://arxiv.org/html/2510.19511v1#S2.E9 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) we find that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0<E​[Pn+1]=Pr⁡[Pn+1=1]<1.0<E\left[P\_{n+1}\right]=\Pr\left[P\_{n+1}=1\right]<1. |  | (10) |

From ([2](https://arxiv.org/html/2510.19511v1#S2.E2 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) it follows then that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0<E​[Wn+1]<∑j=1n+1πj.0<E\left[W\_{n+1}\right]<\sum\_{j=1}^{n+1}\pi\_{j}. |  | (11) |

Finally, from ([7](https://arxiv.org/html/2510.19511v1#S2.E7 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) and ([8](https://arxiv.org/html/2510.19511v1#S2.E8 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0<∑k=1nE​[Pk]=Pr⁡[Pn+1=0]<1.0<\sum\_{k=1}^{n}E\left[P\_{k}\right]=\Pr\left[P\_{n+1}=0\right]<1. |  | (12) |

We will call the administrator as described above an ‘active administrator’,
where ‘active’ means that he is the ‘owner’ of the compensation Wn+1W\_{n+1}. Further in the paper, we will also introduce the ‘passive administrator’
whose compensation Wn+1W\_{n+1} will be redistributed to the agents.

Let us now introduce the (deterministic) investment vector 𝝅\boldsymbol{\pi},
which is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝅=(π1,π2,…,πn+1),\boldsymbol{\pi}=\left(\pi\_{1},\pi\_{2},\ldots,\pi\_{n+1}\right), |  | (13) |

as well as the time 11 measurable compensation vector 𝐖\mathbf{W}, defined
by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐖=(W1,W2,…,Wn+1),\mathbf{W}=\left(W\_{1},W\_{2},\ldots,W\_{n+1}\right), |  | (14) |

and the time 11 measurable relative compensation vector 𝐏\mathbf{P},
defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑷=(P1,P2,…,Pn+1).\boldsymbol{P}=\big(P\_{1},P\_{2},\ldots,P\_{n+1}\big). |  | (15) |

Taking into account the introduced vector notations, we can rewrite ([2](https://arxiv.org/html/2510.19511v1#S2.E2 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing"))
and ([4](https://arxiv.org/html/2510.19511v1#S2.E4 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) in the following way:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑾=(∑j=1n+1πj)×𝑷.\boldsymbol{W}=\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times\boldsymbol{P}. |  | (16) |

In the following definition, we introduce the set of all relative compensation
vectors for the n+1n+1 agents.

###### Definition 1

The set ℛn+1\mathcal{R}\_{n+1} is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛn+1={(P1,P2,…,Pn+1)∈L+0∣∑j=1n+1Pj=1​ and ​Pn+1=1​(∑j=1nPj=0)}.\mathcal{R}\_{n+1}=\left\{\left(P\_{1},P\_{2},\ldots,P\_{n+1}\right)\in L\_{+}^{0}\mid\sum\_{j=1}^{n+1}P\_{j}=1\text{ and }P\_{n+1}={1}\left(\sum\_{j=1}^{n}P\_{j}=0\right)\right\}. |  | (17) |

The set ℛn+1\mathcal{R}\_{n+1} consists of all (n+1)\left(n+1\right)-dimensional relative compensation vectors. Any 𝑾=(∑j=1n+1πj)×𝑷\boldsymbol{W}=\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times\boldsymbol{P}, where 𝑷∈ℛn+1\boldsymbol{P}\in\mathcal{R}\_{n+1} is a reallocation (or redistribution) of the time 11
value of the fund between the nn participants and the administrator, such
that ∑j=1nWj\sum\_{j=1}^{n}W\_{j} and Wn+1W\_{n+1} are mutually exclusive. The latter
condition means that the events ‘at least one WiW\_{i} is positive’ and
‘Wn+1W\_{n+1} is positive’ are mutually exclusive.

Compensation-based RS is a two-stage process. At time 0, any agent makes an initial investment πi\pi\_{i} and their
aggregate investment (∑j=1n+1πj)\left(\sum\_{j=1}^{n+1}\pi\_{j}\right) is reallocated
by transforming 𝝅\boldsymbol{\pi} into random vector 𝑾\boldsymbol{W} defined
in ([16](https://arxiv.org/html/2510.19511v1#S2.E16 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), with 𝑷∈ℛn+1\boldsymbol{P}\in\mathcal{R}\_{n+1}. At time 11, the participants and the administrator receive
the respective realizations of the compensations that were attributed to
them. 
Hereafter, we denote the compensation WiW\_{i} by Wi​[𝝅]W\_{i}\left[\boldsymbol{\pi}\right] and the compensation vector 𝑾\boldsymbol{W} by
𝑾​[𝝅]\boldsymbol{W}\left[\boldsymbol{\pi}\right] in case we want to emphasize
that the underlying investment vector is 𝝅\boldsymbol{\pi}. Similarly, we
write the relative compensation PiP\_{i} by Pi​[𝝅]P\_{i}\left[\boldsymbol{\pi}\right]
and the relative compensation vector 𝑷\boldsymbol{P} by 𝑷​[𝝅]\boldsymbol{P}\left[\boldsymbol{\pi}\right] to denote their dependence on 𝝅\boldsymbol{\pi}.
When the meaning is clear, we will omit the [𝝅]\left[\boldsymbol{\pi}\right] in the notation.

We are now ready to define a compensation-based RS scheme with an active administrator.

###### Definition 2

A compensation-based risk-sharing scheme for a given group of nn participants
and an active administrator is a pair (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right), where 𝛑=(π1,π2,…,πn+1)\boldsymbol{\pi}=\left(\pi\_{1},\pi\_{2},\ldots,\pi\_{n+1}\right) is the initial investment vector, while 𝐏=(P1,P2,…,Pn+1)\boldsymbol{P}=\left(P\_{1},P\_{2},\ldots,P\_{n+1}\right) is a relative compensation
vector, that is 𝐏∈ℛn+1\boldsymbol{P}\in\mathcal{R}\_{n+1}. Moreover, the
compensations attributed to the n+1n+1 agents are expressed by the compensation
vector 𝐖\boldsymbol{W}, which is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wi=(∑j=1n+1πj)×Pii=1,2,…,n+1.W\_{i}=\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times P\_{i}\qquad i=1,2,\ldots,n+1. |  | (18) |

A compensation-based RS scheme with an active administrator is
specified by its investment vector 𝝅\boldsymbol{\pi} and its relative
compensation vector 𝑷\boldsymbol{P} (or its compensation vector
𝑾\boldsymbol{W}). The administrator is called ‘active’ in the sense that he
is entitled to a random compensation at time 11. Further in this paper, we
will also consider a ‘passive’ administrator, who in not entitled to any
random compensation at time 11. We remark that investments are known at time 0, whereas the random compensations remain
unknown until they become observable at time 11. As 𝑷∈ℛn+1\boldsymbol{P}\in\mathcal{R}\_{n+1}, a compensation-based RS scheme with an
active administrator satisfies the following full allocation
condition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑j=1n+1Wj=∑j=1n+1πj,\sum\_{j=1}^{n+1}W\_{j}=\sum\_{j=1}^{n+1}\pi\_{j}, |  | (19) |

which means that such an RS scheme is a fully funded system and has no
insolvency issues: the total amount that will be distributed at time 11 will
also be available at that time.

After having introduced compensation-based RS schemes, we can now
define a compensation-based RS rule as an appropriate set of compensation-based RS schemes.

###### Definition 3

A compensation-based risk-sharing rule for a given group of nn participants
and an active administrator is a mapping 𝐏:(ℝ+)n+1→ℛn+1\boldsymbol{P}:\left(\mathbb{R}^{+}\right)^{n+1}\rightarrow\mathcal{R}\_{n+1} which transforms any
investment vector 𝛑\boldsymbol{\pi} in (ℝ+)n+1\left(\mathbb{R}^{+}\right)^{n+1} into a relative compensation vector 𝐏​[𝛑]\boldsymbol{P}\left[\boldsymbol{\pi}\right]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝅∈(ℝ+)n+1→𝑷​[𝝅]∈ℛn+1.\boldsymbol{\pi}\in\left(\mathbb{R}^{+}\right)^{n+1}\rightarrow\boldsymbol{P}\left[\boldsymbol{\pi}\right]\in\mathcal{R}\_{n+1}. |  | (20) |

In this paper, when we consider a ‘RS scheme’ or a ‘RS rule’, we always mean a
‘compensation-based RS scheme’ or a ‘compensation-based RS rule’.

## 3 Some examples

In this section, we illustrate the concept of compensation-based RS with an
active administrator with some examples.

###### Example 1

Suppose that each participant ii of a group of nn individuals is exposed to
a (random) non-negative loss XiX\_{i} at time 11. The nn participants decide
to share the risk related to these losses amongst themselves. Therefore, they
appoint an administrator, called agent n+1n+1, and set up an RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right), with

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pi=Xi∑j=1n+1Xj,i=1,2,…,n+1,P\_{i}=\frac{X\_{i}}{\sum\_{j=1}^{n+1}X\_{j}},\qquad i=1,2,\ldots,n+1, |  | (21) |

with Xn+1X\_{n+1} defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xn+1=1​(∑j=1nXj=0).X\_{n+1}=1\left(\sum\_{j=1}^{n}X\_{j}=0\right). |  | (22) |

It is easy to see that Xn+1X\_{n+1} and ∑j=1nXj\sum\_{j=1}^{n}X\_{j} are mutually
exclusive. This mutual exclusivity property implies that the denominator in
([21](https://arxiv.org/html/2510.19511v1#S3.E21 "In Example 1 ‣ 3 Some examples ‣ Compensation-based risk-sharing")) is never equal to 0, so that the PiP\_{i}’s are always well-defined. Obviously, the mutual exclusivity of (Xn+1,∑j=1nXj)\left(X\_{n+1},\sum\_{j=1}^{n}X\_{j}\right) is equivalent to the mutual exclusivity of (Pn+1,∑j=1nPj)\left(P\_{n+1},\sum\_{j=1}^{n}P\_{j}\right), which is equivalent to the mutual
exclusivity of (Wn+1,∑j=1nWj)\left(W\_{n+1},\sum\_{j=1}^{n}W\_{j}\right).
  
The
participants in the RS scheme with relative compensation vector defined by ([21](https://arxiv.org/html/2510.19511v1#S3.E21 "In Example 1 ‣ 3 Some examples ‣ Compensation-based risk-sharing"))
share the proceeds of the fund proportionally, where each participant’s
proportion is equal to the proportion that he contributes to aggregate claims
∑j=1n+1Xj\sum\_{j=1}^{n+1}X\_{j}. On the other hand, the administrator receives the
full proceeds of the fund in case all participants experience a zero loss,
whereas he receives nothing in the other case. Typically, insurance losses
have a strictly positive probability mass at zero, implying that our
assumption that Pr⁡[Pn+1=1]>0\Pr\left[P\_{n+1}=1\right]>0 is reasonable.
  
Remark that the compensations WiW\_{i} defined via the relative compensations
([21](https://arxiv.org/html/2510.19511v1#S3.E21 "In Example 1 ‣ 3 Some examples ‣ Compensation-based risk-sharing")) can be expressed as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wi=∑j=1n+1πj∑j=1n+1Xj×Xi,i=1,2,…,n+1.W\_{i}=\frac{\sum\_{j=1}^{n+1}\pi\_{j}}{\sum\_{j=1}^{n+1}X\_{j}}\times X\_{i},\qquad i=1,2,\ldots,n+1. |  | (23) |

This means that the RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) is such that each participant ii is compensated the same time 11
observable proportion of his loss XiX\_{i}, while the administrator receives the full proceeds of the fund in case each participant has a zero claim. This seems to be a reasonable way to distribute the total fund over the n+1n+1 agents, provided each
agent’s initial investment πi\pi\_{i} is ‘reasonable’ or ‘fair’. In Section 4, we
introduce and investigate ‘actuarially fair’ initial investments. ⊲\vartriangleleft

###### Example 2

Consider a group of nn participants. Each of them may experience a
particular event of a given type in the observation period [0,1]\left[0,1\right]. Possible events include the participant’s death, survival,
being hospitalized, being diagnosed with a critical illness, etc. For
simplicity, hereafter we will assume that all predefined events are ‘survival
to time 11’, but any other choice for the predefined events is possible. For
each participant ii, we introduce the indicator variable IiI\_{i}, which is
defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ii={1:i​ survives until time ​10:i​ dies before time ​1I\_{i}=\left\{\begin{array}[c]{ll}1&:i\text{ survives until time }1\\ 0&:i\text{ dies before time }1\end{array}\right. |  | (24) |

The participants appoint an active administrator and attach the following
indicator variable In+1I\_{n+1} to him:

|  |  |  |  |
| --- | --- | --- | --- |
|  | In+1=∏j=1n(1−Ij).I\_{n+1}={\displaystyle\prod\limits\_{j=1}^{n}}\left(1-I\_{j}\right).\ |  | (25) |

We further introduce the notation pi=Pr⁡[Ii=1]p\_{i}=\Pr\left[I\_{i}=1\right] and qi=Pr⁡[Ii=0],i=1,…,n+1q\_{i}=\Pr\left[I\_{i}=0\right],\hskip 5.69054pti=1,\ldots,n+1. Obviously, ∑j=1nIj\sum\_{j=1}^{n}I\_{j} and In+1I\_{n+1} are mutually exclusive. The
participants decide to set up an RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right), with the relative compensation vector
𝐏\boldsymbol{P} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pi=fi×Ii∑j=1n+1fj×Ij,i=1,2,…,n+1,P\_{i}=\frac{f\_{i}\times I\_{i}}{\sum\_{j=1}^{n+1}f\_{j}\times I\_{j}},\qquad i=1,2,\ldots,n+1, |  | (26) |

where fif\_{i}, for i=1,2,…,n+1i=1,2,\ldots,n+1, are strictly positive real
numbers.
  
The RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) defined via the relative compensations ([26](https://arxiv.org/html/2510.19511v1#S3.E26 "In Example 2 ‣ 3 Some examples ‣ Compensation-based risk-sharing")) is a special
case of the RS scheme considered in Example 1. Such RS schemes with an active
administrator have been investigated in detail in Dhaene and Milevsky (2024),
who investigate fair methods for the surviving participants to share the total
investment among themselves if one or more survive. In case all participants
pass away, the administrator receives the full proceeds of the fund. An RS
scheme of this type is often called a tontine fund. Dhaene and Milevsky
(2024) call fif\_{i} the number of tontine shares invested in the
tontine fund, and describe the RS scheme defined by ([26](https://arxiv.org/html/2510.19511v1#S3.E26 "In Example 2 ‣ 3 Some examples ‣ Compensation-based risk-sharing")) as a scheme
where the proceeds of the fund are equally shared among all surviving tontine
shares, where the total number of surviving tontine shares is given by the
denominator in ([26](https://arxiv.org/html/2510.19511v1#S3.E26 "In Example 2 ‣ 3 Some examples ‣ Compensation-based risk-sharing")). They consider the situation where initial
investments (wealth) and survival probabilities (health) vary among
participants, which is called the heterogeneous case. As a special case, they
also examine the situation where all participants invest the same amount and
the random variables I1,I2,…,InI\_{1},I\_{2},\ldots,I\_{n} are i.i.d., which they refer to as the
homogeneous case. Denuit and Robert (2025) consider a similar scheme (with a
passive administrator, see further), where the fif\_{i} are related to (what
they call) protection units from the investment fund, and where the
total value of the tontine fund is divided equally among all claiming
units. An essential difference between the two approaches is that
Dhaene and Milevsky (2024) introduce the active administrator who contributes
to the investments and will own the proceeds of the fund in case not any
person survives, whereas Denuit and Robert (2025) assume a passive
administrator who does not contribute to the investments, and in case nobody
experiences the event under consideration, participants receive their initial
investment back. We will come back to this essential difference between the
two approaches in a further section of this paper.
  
Special cases of
the RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) defined via
the relative compensations ([26](https://arxiv.org/html/2510.19511v1#S3.E26 "In Example 2 ‣ 3 Some examples ‣ Compensation-based risk-sharing")) have been considered in several papers. Dhaene and
Milevsky (2024) consider the following choices for the claiming units fif\_{i}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | fiDM=πipi,i=1,2,…,n+1.f\_{i}^{\text{DM}}=\frac{\pi\_{i}}{p\_{i}},\qquad i=1,2,\ldots,n+1. |  | (27) |

Tavin (2023) proposes the following set of fif\_{i}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | fiT=πi,i=1,2,…,n+1.f\_{i}^{\text{T}}=\pi\_{i},\qquad i=1,2,\ldots,n+1. |  | (28) |

Denuit and Robert (2023) also consider the case of uniform fif\_{i}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | fiDR=1,i=1,2,…,n+1.f\_{i}^{\text{DR}}=1,\qquad i=1,2,\ldots,n+1. |  | (29) |

Finally, in Dhaene and Milevsky (2024), the RS scheme with

|  |  |  |
| --- | --- | --- |
|  | fi=1pi,i=1,2,…,n+1f\_{i}=\frac{1}{p\_{i}},\qquad i=1,2,\ldots,n+1 |  |

is also considered. Interpretations and motivations for any of these choices for the number of
claiming units fif\_{i} can be found in the above-mentioned papers.
  
We remark that the compensation vector 𝐖\boldsymbol{W} with relative
compensation vector determined by ([26](https://arxiv.org/html/2510.19511v1#S3.E26 "In Example 2 ‣ 3 Some examples ‣ Compensation-based risk-sharing")) can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wi=(∑k​1n+1πk∑j=1n+1fj×Ij)×fi×Ii,i=1,2,…,n+1.W\_{i}=\left(\frac{\sum\_{k1}^{n+1}\pi\_{k}}{\sum\_{j=1}^{n+1}f\_{j}\times I\_{j}}\right)\times f\_{i}\times I\_{i},\qquad i=1,2,\ldots,n+1. |  | (30) |

This means that under the RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) defined by ([26](https://arxiv.org/html/2510.19511v1#S3.E26 "In Example 2 ‣ 3 Some examples ‣ Compensation-based risk-sharing")), each surviving participant ii is
compensated the same time 11 observable proportion of his surviving shares or
protection units fif\_{i}. The proportion is the random payment
per claiming protection unit, which is determined such that the full
allocation condition is fulfilled. ⊲\hfill\vartriangleleft

###### Example 3

Consider the loss vector (X1,X2,…,Xn)\left(X\_{1},X\_{2},\ldots,X\_{n}\right),
describing the non-negative losses of the nn participants in the observation
period [0,1]\left[0,1\right]. The ii-th order statistic X(i)X\_{(i)} of
(X1,X2,…,Xn)\left(X\_{1},X\_{2},\ldots,X\_{n}\right) is the ii-th smallest value in
(X1,X2,…,Xn)\left(X\_{1},X\_{2},\ldots,X\_{n}\right). Hence,

|  |  |  |
| --- | --- | --- |
|  | X(1)≤X(2)≤⋯≤X(n).X\_{(1)}\leq X\_{(2)}\leq\cdots\leq X\_{(n)}. |  |

Furthermore, we define X(n+1)X\_{(n+1)} as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | X(n+1)=1​(∑j=1nXj=0).X\_{(n+1)}=1\left(\sum\_{j=1}^{n}X\_{j}=0\right). |  | (31) |

Notice that we only consider the order statistics for the losses of the nn
participants. The random variable X(n+1)X\_{(n+1)} defined above is not an order
statistic. The notation X(n+1)X\_{(n+1)} is introduced only to make notations
uniform and simple.
  
Suppose that the participants set up a fund in
which each participant ii invests an amount πi\pi\_{i}. Moreover, they appoint an
administrator, who contributes the amount πn+1\pi\_{n+1} to the fund. The n+1n+1
agents determine the compensations according to the risk-sharing scheme
(𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right), with relative compensation
vector 𝐏\boldsymbol{P} determined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pi=X(i)∑j=1n+1X(j),i=1,2,…,n+1.P\_{i}=\frac{X\_{(i)}}{\sum\_{j=1}^{n+1}X\_{(j)}},\qquad i=1,2,\ldots,n+1. |  | (32) |

The interpretation of this compensation-based RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) is as follows. For participants
who are ordered in decreasing risk-bearing capacity (e.g., decreasing wealth
or decreasing age), a lower risk-bearing capacity leads to a higher
compensation. In case all participants have a zero-claim, the proceeds of the
fund are fully transferred to the administrator. ⊲\hfill\vartriangleleft

###### Example 4

Consider the vector (X1,X2,…,Xn)\left(X\_{1},X\_{2},\ldots,X\_{n}\right), describing
the non-negative losses of the nn participants in the observation period
[0,1]\left[0,1\right]. The participants set up a fund in which each participant ii
invests an amount πi\pi\_{i}. They also appoint an administrator, who
contributes the amount πn+1\pi\_{n+1} to the fund. The participants and the administrator decide to
share the proceeds of the fund according to the RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right), with the relative compensation
vector 𝐏\boldsymbol{P} being (X1,X2,…,Xn)\left(X\_{1},X\_{2},\ldots,X\_{n}\right) -
measurable. This means that the randomness of 𝐏\boldsymbol{P} is only due to
the randomness of the vector (X1,X2,…,Xn)\left(X\_{1},X\_{2},\ldots,X\_{n}\right). Hence, there exist functions gi:g\_{i}: (ℝ+)n→ℝ+\left(\mathbb{R}^{+}\right)^{n}\rightarrow\mathbb{R}^{+} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pi=gi​(X1,X2,…,Xn),i=1,…,n+1.P\_{i}=g\_{i}\left(X\_{1},X\_{2},\ldots,X\_{n}\right),\qquad i=1,\ldots,n+1. |  | (33) |

Notice that the relative compensation vector will in general also depend on
the initial investment vector 𝛑\boldsymbol{\pi} of the RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) under consideration. But as
𝛑\boldsymbol{\pi} is fixed, we do not explicitly indicate the dependence of
𝛑\boldsymbol{\pi} in the notation of the relative compensation vector. The
full allocation condition ([7](https://arxiv.org/html/2510.19511v1#S2.E7 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) can now be expressed
as follows:

|  |  |  |
| --- | --- | --- |
|  | ∑i=1n+1gj​(X1,X2,…,Xn)=1.\sum\_{i=1}^{n+1}g\_{j}\left(X\_{1},X\_{2},\ldots,X\_{n}\right)=1. |  |

Moreover, the relative compensation vector is assumed to satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | gn+1​(X1,X2,…,Xn)=1​(∑j=1ngj​(X1,X2,…,Xn)=0),g\_{n+1}\left(X\_{1},X\_{2},\ldots,X\_{n}\right)=1\left(\sum\_{j=1}^{n}g\_{j}\left(X\_{1},X\_{2},\ldots,X\_{n}\right)=0\right), |  | (34) |

which means that ∑i=1ngi​(X1,X2,…,Xn)\sum\_{i=1}^{n}g\_{i}\left(X\_{1},X\_{2},\ldots,X\_{n}\right) and gn+1​(X1,X2,…,Xn)g\_{n+1}\left(X\_{1},X\_{2},\ldots,X\_{n}\right) are mutually
exclusive.
  
The RS scheme considered in Example 1 is a special case of ([33](https://arxiv.org/html/2510.19511v1#S3.E33 "In Example 4 ‣ 3 Some examples ‣ Compensation-based risk-sharing")), with the relative compensation vector determined from

|  |  |  |
| --- | --- | --- |
|  | Pi=gi​(X1,X2,…,Xn)=Xi∑j=1n+1Xj,i=1,…,n+1,P\_{i}=g\_{i}\left(X\_{1},X\_{2},\ldots,X\_{n}\right)=\frac{X\_{i}}{\sum\_{j=1}^{n+1}X\_{j}},\qquad i=1,\ldots,n+1, |  |

with Xn+1X\_{n+1} given by ([22](https://arxiv.org/html/2510.19511v1#S3.E22 "In Example 1 ‣ 3 Some examples ‣ Compensation-based risk-sharing")).
  
Also the RS scheme considered
in Example 2 is a special case, with the relative compensations defined by

|  |  |  |
| --- | --- | --- |
|  | Pi=gi​(X1,X2,…,Xn)=fi×Ii∑j=1n+1fj×Ij,i=1,…,n+1,P\_{i}=g\_{i}\left(X\_{1},X\_{2},\ldots,X\_{n}\right)=\frac{f\_{i}\times I\_{i}}{\sum\_{j=1}^{n+1}f\_{j}\times I\_{j}},\qquad i=1,\ldots,n+1, |  |

with the Bernoulli random variables IiI\_{i} as defined in ([24](https://arxiv.org/html/2510.19511v1#S3.E24 "In Example 2 ‣ 3 Some examples ‣ Compensation-based risk-sharing")) and ([25](https://arxiv.org/html/2510.19511v1#S3.E25 "In Example 2 ‣ 3 Some examples ‣ Compensation-based risk-sharing")).
  
Another special case of ([33](https://arxiv.org/html/2510.19511v1#S3.E33 "In Example 4 ‣ 3 Some examples ‣ Compensation-based risk-sharing")) arises by making the
following choice for the relative compensations:

|  |  |  |
| --- | --- | --- |
|  | Pi=gi​(X1,X2,…,Xn)=X(i)∑j=1n+1X(j),i=1,…,n+1,P\_{i}=g\_{i}\left(X\_{1},X\_{2},\ldots,X\_{n}\right)=\frac{X\_{(i)}}{\sum\_{j=1}^{n+1}X\_{(j)}},\qquad i=1,\ldots,n+1, |  |

where X(n+1)X\_{(n+1)} is defined in ([31](https://arxiv.org/html/2510.19511v1#S3.E31 "In Example 3 ‣ 3 Some examples ‣ Compensation-based risk-sharing")). This special case was considered
in Example 3. ⊲\hfill\vartriangleleft

## 4 Actuarial fairness of compensation-based risk-sharing with an active administrator

### 4.1 Actuarially fair risk-sharing schemes

An RS scheme (𝝅,𝑷)\left(\boldsymbol{\pi},\boldsymbol{P}\right) is said to be
actuarially fair for the participants if the time 11 value of each
participant’s initial investment πi\pi\_{i} in the fund is equal to the
expected value of the compensation WiW\_{i} that he will receive at time 11.
This means that no participant experiences a gain or loss on average by
joining the pool. Actuarial fairness of particular compensation-based RS
schemes has been investigated in Bernard et al. (2024), Milevsky and Dhaene
(2024) and Denuit and Robert (2025), amongst others.

###### Definition 4

The RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with an
active administrator is actuarially fair for each participant if the following
conditions hold:

|  |  |  |
| --- | --- | --- |
|  | πi=E​[Wi],i=1,2,…,n.\pi\_{i}=E\left[W\_{i}\right],\qquad i=1,2,\ldots,n. |  |

Taking into account ([18](https://arxiv.org/html/2510.19511v1#S2.E18 "In Definition 2 ‣ 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), we can rewrite the actuarial fairness
conditions for the nn participants as

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi=(∑j=1n+1πj)×E​[Pi],i=1,2,…,n.\pi\_{i}=\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times E\left[P\_{i}\right],\qquad i=1,2,\ldots,n. |  | (35) |

Notice that in a real world context, the particular RS scheme that is chosen
by a group of participants may depend on the social cohesion between them,
ranging from solidarity to pure individualism. Especially in small pools of
connected participants (e.g., family members), actuarial fairness may not be
the first concern and may be replaced by a form of organized transfer, e.g.,
from the elder participants to the younger, or from the richer to the poorer
ones. In this section however, we will further investigate actuarial fairness
of RS schemes.

In our general compensation-based RS set-up with an active administrator,
all proceeds of the fund are transferred to the administrator in case no
participant receives a positive compensation. In return, the administrator
pays an initial investment πn+1\pi\_{n+1} for this benefit. Let us now define
actuarial fairness for the administrator.

###### Definition 5

The RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with an active administrator is
actuarially fair for the active administrator if

|  |  |  |
| --- | --- | --- |
|  | πn+1=E​[Wn+1].\pi\_{n+1}=E\left[W\_{n+1}\right]. |  |

Taking into account ([10](https://arxiv.org/html/2510.19511v1#S2.E10 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) and ([18](https://arxiv.org/html/2510.19511v1#S2.E18 "In Definition 2 ‣ 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), we can rewrite this
actuarial fairness condition for the administrator as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | πn+1=(∑j=1n+1πj)×Pr⁡[Pn+1=1].\pi\_{n+1}=\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times\Pr\left[P\_{n+1}=1\right]. |  | (36) |

As Pr⁡[Pn+1=0]\Pr\left[P\_{n+1}=0\right] is strictly positive by assumption, see
([8](https://arxiv.org/html/2510.19511v1#S2.E8 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), the actuarial fairness condition for the administrator can also
be expressed as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | πn+1=(∑j=1nπj)×Pr⁡[Pn+1=1]Pr⁡[Pn+1=0].\pi\_{n+1}=\left(\sum\_{j=1}^{n}\pi\_{j}\right)\times\frac{\Pr\left[P\_{n+1}=1\right]}{\Pr\left[P\_{n+1}=0\right]}. |  | (37) |

In case the relative compensations PiP\_{i} of the participants are i.i.d., we have
that

|  |  |  |
| --- | --- | --- |
|  | Pr⁡[Pn+1=1]=Pr⁡[P1=P2=⋯=Pn=0]=(Pr⁡[P1=0])n.\Pr\left[P\_{n+1}=1\right]=\Pr\left[P\_{1}=P\_{2}=\cdots=P\_{n}=0\right]=\left(\Pr\left[P\_{1}=0\right]\right)^{n}. |  |

This means that if the number of participants nn is sufficiently large, we
find that Pr⁡[Pn+1=1]≈0\Pr\left[P\_{n+1}=1\right]\approx 0 and Pr⁡[Pn+1=0]≈1\Pr\left[P\_{n+1}=0\right]\approx 1, which implies that the actuarially fair initial
investment πn+1\pi\_{n+1} of the administrator is close to zero.

Let us now consider the relation between actuarial fairness for the
participants and actuarial fairness for the active administrator.

###### Proposition 1

If the RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) is
actuarially fair for the nn participants, then it is also actuarially fair
for the active administrator.

Proof: From the actuarial fairness conditions ([35](https://arxiv.org/html/2510.19511v1#S4.E35 "In 4.1 Actuarially fair risk-sharing schemes ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) for the nn participants,
we find that

|  |  |  |
| --- | --- | --- |
|  | ∑k=1nπk=(∑j=1n+1πj)×∑k=1nE​[Pk].\sum\_{k=1}^{n}\pi\_{k}=\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times\sum\_{k=1}^{n}E\left[P\_{k}\right]. |  |

Taking into account ([12](https://arxiv.org/html/2510.19511v1#S2.E12 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) leads to the actuarial fairness condition
([37](https://arxiv.org/html/2510.19511v1#S4.E37 "In 4.1 Actuarially fair risk-sharing schemes ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) for the administrator.

From the previous proposition, we can conclude that if the RS scheme (𝝅,𝑷)\left(\boldsymbol{\pi},\boldsymbol{P}\right) is not actuarially fair for the active
administrator, then it can also not be actuarially fair for all
participants. In particular, this situation will occur in case the
administrator makes an investment of zero. This observation is further
explored in the following proposition.

###### Proposition 2

If the active administrator of the RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) makes a zero initial investment, i.e., πn+1=0\pi\_{n+1}=0, then there must be at least one participant ii whose investment πi\pi\_{i} exceeds his
expected compensation, i.e., πi>E​[Wi]\pi\_{i}>E\left[W\_{i}\right].

Proof: In case πn+1=0\pi\_{n+1}=0, we find from the full allocation condition ([19](https://arxiv.org/html/2510.19511v1#S2.E19 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing"))
that

|  |  |  |
| --- | --- | --- |
|  | ∑j=1nπj=∑j=1n+1E​[Wj].\sum\_{j=1}^{n}\pi\_{j}=\sum\_{j=1}^{n+1}E\left[W\_{j}\right]. |  |

Furthermore, from ([11](https://arxiv.org/html/2510.19511v1#S2.E11 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), we have that E​[Wn+1]>0E\left[W\_{n+1}\right]>0. This means that for at least one participant ii, one must have that his
investment exceeds his expected compensation, that is, for at least on
participant ii one must have that πi>E​[Wi]\pi\_{i}>E\left[W\_{i}\right].

In the following proposition, we consider several necessary and sufficient
conditions for actuarial fairness for the n+1n+1 agents involved in the RS
scheme (𝝅,𝑷)\left(\boldsymbol{\pi},\boldsymbol{P}\right).

###### Proposition 3

The RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with active
administrator is actuarially fair for the n+1n+1 agents if and only if any of the
following conditions is satisfied:
  
Condition 1: The RS scheme
(𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi=(∑j=1n+1πj)×E​[Pi],i=1,2,…,n+1.\pi\_{i}=\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times E\left[P\_{i}\right],\qquad i=1,2,\ldots,n+1. |  | (38) |

  

Condition 2: The RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi=(∑j=1nπj)×E​[Pi]Pr⁡[Pn+1=0],i=1,2,…,n+1.\pi\_{i}=\left(\sum\_{j=1}^{n}\pi\_{j}\right)\times\frac{E\left[P\_{i}\right]}{\Pr\left[P\_{n+1}=0\right]},\qquad i=1,2,\ldots,n+1. |  | (39) |

  

Condition 3: The RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi=πn+1×E​[Pi]Pr⁡[Pn+1=1],i=1,2,…,n+1.\pi\_{i}=\pi\_{n+1}\times\frac{E\left[P\_{i}\right]}{\Pr\left[P\_{n+1}=1\right]},\qquad i=1,2,\ldots,n+1. |  | (40) |

Proof: Actuarial fairness for all agents is, by definition, equivalent to Condition
1.
  
Condition 1⇒1\Rightarrow Condition
33: Suppose that Condition 11 holds for the n+1n+1 agents. Then,
taking into account ([10](https://arxiv.org/html/2510.19511v1#S2.E10 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | πn+1=(∑j=1n+1πj)×Pr⁡[Pn+1=1].\pi\_{n+1}=\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times\Pr\left[P\_{n+1}=1\right]. |  | (41) |

Substituting (∑j=1n+1πj)\left(\sum\_{j=1}^{n+1}\pi\_{j}\right) by πn+1Pr⁡[Pn+1=1]\frac{\pi\_{n+1}}{\Pr\left[P\_{n+1}=1\right]} in the relations ([38](https://arxiv.org/html/2510.19511v1#S4.E38 "In Proposition 3 ‣ 4.1 Actuarially fair risk-sharing schemes ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) for the nn
participants, leads to the relations ([40](https://arxiv.org/html/2510.19511v1#S4.E40 "In Proposition 3 ‣ 4.1 Actuarially fair risk-sharing schemes ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) for i=1,2,…,ni=1,2,\ldots,n. Obviously, ([40](https://arxiv.org/html/2510.19511v1#S4.E40 "In Proposition 3 ‣ 4.1 Actuarially fair risk-sharing schemes ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) also holds for n+1n+1. We can conclude that
Condition 11 implies Condition 33.Condition
3⇒3\Rightarrow Condition 22: Suppose that Condition 33 holds.
Taking into account ([12](https://arxiv.org/html/2510.19511v1#S2.E12 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), we find that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑j=1nπj\displaystyle\sum\_{j=1}^{n}\pi\_{j} | =πn+1×∑j=1nE​[Pj]Pr⁡[Pn+1=1]\displaystyle=\pi\_{n+1}\times\frac{\sum\_{j=1}^{n}E\left[P\_{j}\right]}{\Pr\left[P\_{n+1}=1\right]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =πn+1×Pr⁡[Pn+1=0]Pr⁡[Pn+1=1],\displaystyle=\pi\_{n+1}\times\frac{\Pr\left[P\_{n+1}=0\right]}{\Pr\left[P\_{n+1}=1\right]}, |  |

which means that Condition 22 holds for agent n+1n+1. Substituting πn+1Pr⁡[Pn+1=1]\frac{\pi\_{n+1}}{\Pr\left[P\_{n+1}=1\right]} by ∑j=1nπjPr⁡[Pn+1=0]\frac{\sum\_{j=1}^{n}\pi\_{j}}{\Pr\left[P\_{n+1}=0\right]} in the relations ([40](https://arxiv.org/html/2510.19511v1#S4.E40 "In Proposition 3 ‣ 4.1 Actuarially fair risk-sharing schemes ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) for the nn
participants shows that the relation ([39](https://arxiv.org/html/2510.19511v1#S4.E39 "In Proposition 3 ‣ 4.1 Actuarially fair risk-sharing schemes ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) also hold for each of
them. We can conclude that Condition 33 implies Condition 22.
  
Condition 2⇒2\Rightarrow Condition 11: Suppose
that Condition 22 holds. Then we find that

|  |  |  |
| --- | --- | --- |
|  | (∑j=1n+1πj)=(∑j=1nπj)×1Pr⁡[Pn+1=0].\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)=\left(\sum\_{j=1}^{n}\pi\_{j}\right)\times\frac{1}{\Pr\left[P\_{n+1}=0\right]}. |  |

Substituting ∑j=1nπj\sum\_{j=1}^{n}\pi\_{j} by (∑j=1n+1πj)×Pr⁡[Pn+1=0]\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times\Pr\left[P\_{n+1}=0\right] in the relations
([39](https://arxiv.org/html/2510.19511v1#S4.E39 "In Proposition 3 ‣ 4.1 Actuarially fair risk-sharing schemes ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) for the n+1n+1 agents leads to the relation ([38](https://arxiv.org/html/2510.19511v1#S4.E38 "In Proposition 3 ‣ 4.1 Actuarially fair risk-sharing schemes ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) for each
them, which means that Condition 22 implies Condition 11. This ends the proof.

### 4.2 Risk-sharing rules and actuarial fairness

So far, we have considered the actuarial fairness of a given RS scheme
(𝝅,𝑷)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with active administrator.
Let us now consider an RS rule 𝑷\boldsymbol{P} with an active
administrator, which transforms any investment vector 𝝅\boldsymbol{\pi} into
a relative compensation vector 𝑷​[𝝅]\boldsymbol{P}\left[\boldsymbol{\pi}\right]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝅→𝑷​[𝝅]​.\boldsymbol{\pi}\rightarrow\boldsymbol{P}\left[\boldsymbol{\pi}\right]\text{.} |  | (42) |

This means that any investment vector 𝝅\boldsymbol{\pi} leads to the
compensation vector 𝑾​[𝝅]\boldsymbol{W}\left[\boldsymbol{\pi}\right], with

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑾​[𝝅]=(∑j=1n+1πj)×𝑷​[𝝅]​,\boldsymbol{W}\left[\boldsymbol{\pi}\right]=\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times\boldsymbol{P}\left[\boldsymbol{\pi}\right]\text{,} |  | (43) |

see Definition 3. Let us now consider a special type of RS rules
𝑷\boldsymbol{P}, which satisfy the following indifference property:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑷​[c×𝝅]=𝑷​[𝝅]​, for any ​c>0​ and any investment vector ​𝝅​.\boldsymbol{P}\left[c\times\boldsymbol{\pi}\right]=\boldsymbol{P}\left[\boldsymbol{\pi}\right]\text{,}\qquad\text{\ for any }c>0\text{ and any investment vector }\boldsymbol{\pi}\text{.} |  | (44) |

This means that the RS rule 𝑷\boldsymbol{P} is such that if all participants
increase their initial investment by a constant proportion, e.g., by 20%, then
their relative compensation vector remains unchanged, which seems to be a
reasonable property. Obviously any RS rule of which the relative compensation vector 𝑷\boldsymbol{P} is independent of the initial investment vector satisfies the indifference property ([44](https://arxiv.org/html/2510.19511v1#S4.E44 "In 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")). In the following proposition, we consider contribution
vectors of an RS rule 𝑷\boldsymbol{P} that satisfies the indifference property
([44](https://arxiv.org/html/2510.19511v1#S4.E44 "In 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")).

###### Proposition 4

Consider the RS rule 𝐏\boldsymbol{P} with active administrator that
satisfies the indifference property ([44](https://arxiv.org/html/2510.19511v1#S4.E44 "In 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")). Then for any positive cc
and any investment vector 𝛑\boldsymbol{\pi}, one has that

|  |  |  |
| --- | --- | --- |
|  | 𝐖​[c×𝝅]=c×𝐖​[𝝅]\mathbf{W}\left[c\times\boldsymbol{\pi}\right]=c\times\mathbf{W}\left[\boldsymbol{\pi}\right] |  |

Proof: For any investment vector 𝝅\boldsymbol{\pi}, any c>0c>0 and any participant ii, we
find that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wi​[c×𝝅]\displaystyle W\_{i}\left[c\times\boldsymbol{\pi}\right] | =c×(∑j=1n+1πj)×Pi​[c×𝝅]\displaystyle=c\times\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times P\_{i}\left[c\times\boldsymbol{\pi}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c×(∑j=1n+1πj)×Pi​[𝝅]\displaystyle=c\times\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times P\_{i}\left[\boldsymbol{\pi}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c×Wi​[𝝅].\displaystyle=c\times W\_{i}\left[\boldsymbol{\pi}\right]. |  |

This ends the proof.

Suppose now that a group of participants decides to use the RS rule 𝑷\boldsymbol{P}
with an active administrator, which satisfies the indifference property
([44](https://arxiv.org/html/2510.19511v1#S4.E44 "In 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")). The next question they have to answer is then what particular
initial investment vector 𝝅\boldsymbol{\pi} to choose. It may be reasonable
to select an investment vector 𝝅\boldsymbol{\pi} such that the RS scheme
(𝝅,𝑷​[𝝅])\left(\boldsymbol{\pi},\boldsymbol{P}\left[\boldsymbol{\pi}\right]\right) is actuarially fair. In the following proposition, we show that
this problem has in general no unique solution.

###### Proposition 5

Consider the RS rule 𝐏\boldsymbol{P} with an active administrator satisfying
the indifference property ([44](https://arxiv.org/html/2510.19511v1#S4.E44 "In 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")). Suppose that the RS scheme (𝛑∗,𝐏​[𝛑∗])\left(\boldsymbol{\pi}^{\ast},\boldsymbol{P}\left[\boldsymbol{\pi}^{\ast}\right]\right)\boldsymbol{\ }is actuarially fair for all participants, then for any
c>0c>0, also the RS scheme (c×𝛑∗,𝐏​[c×𝛑∗])\left(c\times\boldsymbol{\pi}^{\ast},\boldsymbol{P}\left[c\times\boldsymbol{\pi}^{\ast}\right]\right) is
actuarially fair for all participants.

Proof: From Proposition 4, we find for any participant ii that

|  |  |  |
| --- | --- | --- |
|  | E​[Wi​[c×𝝅∗]]=c×E​[Wi​[𝝅∗]].E\left[W\_{i}\left[c\times\boldsymbol{\pi}^{\ast}\right]\right]=c\times E\left[W\_{i}\left[\boldsymbol{\pi}^{\ast}\right]\right]. |  |

The actuarial fairness of (𝝅∗,𝑷​[𝝅∗])\left(\boldsymbol{\pi}^{\ast},\boldsymbol{P}\left[\boldsymbol{\pi}^{\ast}\right]\right) can be expressed as

|  |  |  |
| --- | --- | --- |
|  | E​[Wi​[𝝅∗]]=πi∗,i=1,2,…,n+1.E\left[W\_{i}\left[\boldsymbol{\pi}^{\ast}\right]\right]=\pi\_{i}^{\ast},\qquad i=1,2,\ldots,n+1. |  |

Combining both expressions leads to

|  |  |  |
| --- | --- | --- |
|  | E​[Wi​[c×𝝅∗]]=c×πi∗,i=1,2,…,n+1,E\left[W\_{i}\left[c\times\boldsymbol{\pi}^{\ast}\right]\right]=c\times\pi\_{i}^{\ast},\qquad i=1,2,\ldots,n+1, |  |

which are the actuarial fairness conditions for (c×𝝅∗,𝑷​[c×𝝅∗])\left(c\times\boldsymbol{\pi}^{\ast},\boldsymbol{P}\left[c\times\boldsymbol{\pi}^{\ast}\right]\right).

We can conclude that for any RS rule 𝑷\boldsymbol{P} satisfying the
indifference property ([44](https://arxiv.org/html/2510.19511v1#S4.E44 "In 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), one has that if the RS scheme (𝝅∗,𝑷​[𝝅∗])\left(\boldsymbol{\pi}^{\boldsymbol{\ast}},\boldsymbol{P}\left[\boldsymbol{\pi}^{\ast}\right]\right) is actuarially fair for all participants, then also
the RS scheme (c×𝝅∗,𝑷​[c×𝝅∗])\left(c\times\boldsymbol{\pi}^{\ast},\boldsymbol{P}\left[c\times\boldsymbol{\pi}^{\ast}\right]\right) is actuarially fair for all
participants. This means that for such RS rules, actuarially fair investment
vectors 𝝅\boldsymbol{\pi} are only defined up to a positive constant
factor. For RS rules satisfying the independence property ([44](https://arxiv.org/html/2510.19511v1#S4.E44 "In 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")),
Proposition 3 may be a guide for choosing the appropriate actuarially fair set
of initial investments: One can either first determine the level of the
aggregate investments of the n+1n+1 agents, or the level of the aggregate
investment of the nn participants, or the level of the individual investment
of the administrator, and then determine the individual actuarial fair
investments πi\pi\_{i} by the corresponding Conditions 1, 2 or 3.

###### Example 5

In order to illustrate the previous propositions, consider a group of nn
participants who are exposed to the losses X1,X\_{1}, X2,…,XnX\_{2},\ldots,X\_{n},
respectively. Suppose they agree to use the RS rule 𝐏\boldsymbol{P}, where
for any RS scheme (𝛑,𝐏​[𝛑])\left(\boldsymbol{\pi},\boldsymbol{P}\left[\boldsymbol{\pi}\right]\right), the relative compensation vector 𝐏​[𝛑]\boldsymbol{P}\left[\boldsymbol{\pi}\right] is given by ([21](https://arxiv.org/html/2510.19511v1#S3.E21 "In Example 1 ‣ 3 Some examples ‣ Compensation-based risk-sharing")), as considered in
Example 1:

|  |  |  |
| --- | --- | --- |
|  | Pi​[𝝅]=Xi∑k=1n+1Xk,i=1,2,…,n+1,P\_{i}\left[\boldsymbol{\pi}\right]=\frac{X\_{i}}{\sum\_{k=1}^{n+1}X\_{k}},\qquad i=1,2,\ldots,n+1, |  |

with Xn+1X\_{n+1} defined by ([22](https://arxiv.org/html/2510.19511v1#S3.E22 "In Example 1 ‣ 3 Some examples ‣ Compensation-based risk-sharing")). As the random losses X1,X\_{1}, X2,…,XnX\_{2},\ldots,X\_{n} are assumed to be independent of 𝛑\boldsymbol{\pi}, we have that the relative compensation vectors of
the RS rule 𝐏\boldsymbol{P} satisfy the indifference property ([44](https://arxiv.org/html/2510.19511v1#S4.E44 "In 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")).
  
Let us assume that the participants decide to choose an investment
vector 𝛑\boldsymbol{\pi}\ such that the RS scheme (𝛑,𝐏​[𝛑])\left(\boldsymbol{\pi},\boldsymbol{P}\left[\boldsymbol{\pi}\right]\right) is actuarially
fair for any of them. This means that the investment vector follows from the
set of equations ([38](https://arxiv.org/html/2510.19511v1#S4.E38 "In Proposition 3 ‣ 4.1 Actuarially fair risk-sharing schemes ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi=(∑j=1n+1πj)×E​[Xi∑k=1n+1Xk],i=1,2,…,n+1.\pi\_{i}=\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times E\left[\frac{X\_{i}}{\sum\_{k=1}^{n+1}X\_{k}}\right],\qquad i=1,2,\ldots,n+1. |  | (45) |

In this case an actuarially fair investment vector is only defined up to a
positive constant factor, that is, if 𝛑∗\boldsymbol{\pi}^{\ast} is a solution of
([45](https://arxiv.org/html/2510.19511v1#S4.E45 "In Example 5 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), then also c×𝛑∗c\times\boldsymbol{\pi}^{\ast} is a solution, for any
c>0c>0. Applying this RS rule in practice, we could first determine a reference
solution 𝛑\boldsymbol{\pi} of ([45](https://arxiv.org/html/2510.19511v1#S4.E45 "In Example 5 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), and in a second step, determine
the investment vector c×𝛑c\times\boldsymbol{\pi} with cc such that
Pr⁡[c×∑j=1n+1πj>∑j=1n+1Xk]\Pr\left[c\times\sum\_{j=1}^{n+1}\pi\_{j}>\sum\_{j=1}^{n+1}X\_{k}\right]
is sufficiently large. As an extreme case, suppose that cc is chosen
such that Pr⁡[c×∑j=1n+1πj>∑j=1n+1Xk]=1\Pr\left[c\times\sum\_{j=1}^{n+1}\pi\_{j}>\sum\_{j=1}^{n+1}X\_{k}\right]=1, then we have that

|  |  |  |
| --- | --- | --- |
|  | Wi=(c×∑j=1n+1πj)×Xi∑k=1n+1Xk≥Xi,i=1,2,…,n+1,W\_{i}=\left(c\times\sum\_{j=1}^{n+1}\pi\_{j}\right)\times\frac{X\_{i}}{\sum\_{k=1}^{n+1}X\_{k}}\geq X\_{i},\qquad i=1,2,\ldots,n+1, |  |

which means that each compensation WiW\_{i} is always larger than its
corresponding claim XiX\_{i} in this case. ⊲\lhd

###### Example 6

Consider the setting of Example 2 with the number of protection units fif\_{i} chosen to be equal to the initial investment πi\pi\_{i}. This means that we
consider the RS rule 𝐏\boldsymbol{P}, where for any RS scheme (𝛑,𝐏​[𝛑])\left(\boldsymbol{\pi},\boldsymbol{P}\left[\boldsymbol{\pi}\right]\right),
each participant and the administrator receive a level of compensation
proportional to their initial contribution in case the predefined event
occurs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wi​[𝝅]=(∑j=1n+1πj)×πi×Ii∑j=1n+1πj×Ij,i=1,2,…,n+1.W\_{i}\left[\boldsymbol{\pi}\right]=\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times\frac{\pi\_{i}\times I\_{i}}{\sum\_{j=1}^{n+1}\pi\_{j}\times I\_{j}},\qquad i=1,2,\ldots,n+1. |  | (46) |

In these equations, the IiI\_{i} are Bernouilli-distributed random variables with Pr⁡[Ii=1]=pi\Pr\left[I\_{i}=1\right]=p\_{i} and Pr[Ii=0]=qi]\Pr\left[I\_{i}=0\right]=q\_{i}].

We call this rule that was proposed in Tavin (2023) the Tavin RS rule, see
([28](https://arxiv.org/html/2510.19511v1#S3.E28 "In Example 2 ‣ 3 Some examples ‣ Compensation-based risk-sharing")). Obviously, the RS rule 𝐏\boldsymbol{P} satisfies the
indifference property ([44](https://arxiv.org/html/2510.19511v1#S4.E44 "In 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), implying that actuarially fair investments
vectors are only determined up to a positive constant factor. From
([46](https://arxiv.org/html/2510.19511v1#S4.E46 "In Example 6 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) it follows that the actuarial fairness conditions for all participants
in this RS scheme (𝛑,𝐏​[𝛑])\left(\boldsymbol{\pi},\boldsymbol{P}\left[\boldsymbol{\pi}\right]\right) can be written as follows:

|  |  |  |
| --- | --- | --- |
|  | 1=(∑j=1n+1πj)×E​[Ii∑j=1n+1πj×Ij],i=1,2,…,n+1.1=\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times E\left[\frac{I\_{i}}{\sum\_{j=1}^{n+1}\pi\_{j}\times I\_{j}}\right],\qquad i=1,2,\ldots,n+1. |  |

Obviously, for actuarially fair initial investments the expectations E​[Ii∑j=1n+1πj×Ij]E\left[\frac{I\_{i}}{\sum\_{j=1}^{n+1}\pi\_{j}\times I\_{j}}\right]\  have to be equal for all agents. It is important to note the fact that an RS scheme which is not actuarially fair is not necessarily a
‘wrong’ choice. Suppose that two participants of different age each pay the
same initial investment. Then, upon survival, they will receive the same
compensation. However, the one with the higher survival probability (the
younger one, let’s say) will more likely survive and hence, is favored. As
clearly discussed in Tavin (2023), this RS scheme accommodates a reallocation
of wealth that is favorable to those who are likely to survive longer. Such
a reallocation can be a valuable objective, for example, in a given small community of
family members.

###### Example 7

Consider the Tavin RS rule 𝐏\boldsymbol{P} based on
the RS schemes (𝛑,𝐏​[𝛑])\left(\boldsymbol{\pi},\boldsymbol{P}\left[\boldsymbol{\pi}\right]\right) of Example 6, with two participants and an active administrator.

From ([46](https://arxiv.org/html/2510.19511v1#S4.E46 "In Example 6 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) it follows that the actuarial fairness conditions for all participants can be written as follows:

|  |  |  |
| --- | --- | --- |
|  | 1=(π1+π2+π3)×𝔼​[Iiπ1​I1+π2​I2+π3​I3],i=1,2,3.1=(\pi\_{1}+\pi\_{2}+\pi\_{3})\times\mathbb{E}\left[\frac{I\_{i}}{\pi\_{1}I\_{1}+\pi\_{2}I\_{2}+\pi\_{3}I\_{3}}\right],\quad i=1,2,3. |  |

Let us assume that I1I\_{1} and I2I\_{2} are mutually independent. In this setting, we find that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[I1π1​I1+π2​I2+π3​I3]=(p1​p2π1+π2+p1​q2π1),\mathbb{E}\left[\frac{I\_{1}}{\pi\_{1}I\_{1}+\pi\_{2}I\_{2}+\pi\_{3}I\_{3}}\right]=\left(\frac{p\_{1}p\_{2}}{\pi\_{1}+\pi\_{2}}+\frac{p\_{1}q\_{2}}{\pi\_{1}}\right), |  |

while

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[I2π1​I1+π2​I2+π3​I3]=(p1​p2π1+π2+p2​q1π2)\mathbb{E}\left[\frac{I\_{2}}{\pi\_{1}I\_{1}+\pi\_{2}I\_{2}+\pi\_{3}I\_{3}}\right]=\left(\frac{p\_{1}p\_{2}}{\pi\_{1}+\pi\_{2}}+\frac{p\_{2}q\_{1}}{\pi\_{2}}\right) |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[I3π1​I1+π2​I2+π3​I3]=q1​q2π3.\mathbb{E}\left[\frac{I\_{3}}{\pi\_{1}I\_{1}+\pi\_{2}I\_{2}+\pi\_{3}I\_{3}}\right]=\frac{q\_{1}q\_{2}}{\pi\_{3}}. |  |

This results in the following system of equations which characterizes the set of all initial investments (π1,π2,π3)\left(\pi\_{1},\pi\_{2},\pi\_{3}\right) which leads to an actuarially fair Tavin RS scheme ([46](https://arxiv.org/html/2510.19511v1#S4.E46 "In Example 6 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing"))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 1\displaystyle 1 | =(π1+π2+π3)×(p1​p2π1+π2+p1​q2π1)\displaystyle=(\pi\_{1}+\pi\_{2}+\pi\_{3})\times\left(\frac{p\_{1}p\_{2}}{\pi\_{1}+\pi\_{2}}+\frac{p\_{1}q\_{2}}{\pi\_{1}}\right) |  | (47) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 1\displaystyle 1 | =(π1+π2+π3)×(p1​p2π1+π2+p2​q1π2)\displaystyle=(\pi\_{1}+\pi\_{2}+\pi\_{3})\times\left(\frac{p\_{1}p\_{2}}{\pi\_{1}+\pi\_{2}}+\frac{p\_{2}q\_{1}}{\pi\_{2}}\right) |  | (48) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 1\displaystyle 1 | =(π1+π2+π3)×(q1​q2π3).\displaystyle=(\pi\_{1}+\pi\_{2}+\pi\_{3})\times\left(\frac{q\_{1}q\_{2}}{\pi\_{3}}\right). |  | (49) |

From ([47](https://arxiv.org/html/2510.19511v1#S4.E47 "In Example 7 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) and ([48](https://arxiv.org/html/2510.19511v1#S4.E48 "In Example 7 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), we find that

|  |  |  |  |
| --- | --- | --- | --- |
|  | π2=p2​q1p1​q2​π1,\pi\_{2}=\frac{p\_{2}q\_{1}}{p\_{1}q\_{2}}\pi\_{1}, |  | (50) |

while equation ([49](https://arxiv.org/html/2510.19511v1#S4.E49 "In Example 7 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | π1+π2=π3×1−q1​q2q1​q2.\pi\_{1}+\pi\_{2}=\pi\_{3}\times\frac{1-q\_{1}q\_{2}}{q\_{1}q\_{2}}. |  | (51) |

Substituting ([50](https://arxiv.org/html/2510.19511v1#S4.E50 "In Example 7 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) in ([51](https://arxiv.org/html/2510.19511v1#S4.E51 "In Example 7 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) gives rise to

|  |  |  |  |
| --- | --- | --- | --- |
|  | π1=π3×p1q1×1−q1​q2p1​q2+p2​q1,\pi\_{1}=\pi\_{3}\times\frac{p\_{1}}{q\_{1}}\times\frac{1-q\_{1}q\_{2}}{p\_{1}q\_{2}+p\_{2}q\_{1}}, |  | (52) |

and also

|  |  |  |  |
| --- | --- | --- | --- |
|  | π2=π3×p2q2×1−q1​q2p1​q2+p2​q1.\pi\_{2}=\pi\_{3}\times\frac{p\_{2}}{q\_{2}}\times\frac{1-q\_{1}q\_{2}}{p\_{1}q\_{2}+p\_{2}q\_{1}}. |  | (53) |

It is easy to verify that any (π1,π2,π3)\left(\pi\_{1},\pi\_{2},\pi\_{3}\right) with π3>0\pi\_{3}>0 and π1\pi\_{1} and π2\pi\_{2} given by ([52](https://arxiv.org/html/2510.19511v1#S4.E52 "In Example 7 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) and ([53](https://arxiv.org/html/2510.19511v1#S4.E53 "In Example 7 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), respectively, satisfies the system of equations ([47](https://arxiv.org/html/2510.19511v1#S4.E47 "In Example 7 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), ([48](https://arxiv.org/html/2510.19511v1#S4.E48 "In Example 7 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) and ([49](https://arxiv.org/html/2510.19511v1#S4.E49 "In Example 7 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")). We conclude that the set of all initial investments (π1,π2,π3)\left(\pi\_{1},\pi\_{2},\pi\_{3}\right) that lead to an actuarially fair Tavin RS scheme ([46](https://arxiv.org/html/2510.19511v1#S4.E46 "In Example 6 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) with two participants is characterized by ([52](https://arxiv.org/html/2510.19511v1#S4.E52 "In Example 7 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) and ([53](https://arxiv.org/html/2510.19511v1#S4.E53 "In Example 7 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), where π3\pi\_{3} can be any positive real number.

###### Example 8

We end this subsection by considering the RS rule 𝐏\boldsymbol{P} based on
the RS schemes (𝛑,𝐏​[𝛑])\left(\boldsymbol{\pi},\boldsymbol{P}\left[\boldsymbol{\pi}\right]\right) of Example 2, with constant number of protection units for each participant:

|  |  |  |
| --- | --- | --- |
|  | fi=1,i=1,2,…,n+1.f\_{i}=1,\qquad i=1,2,\ldots,n+1. |  |

This means that the RS rule 𝐏\boldsymbol{P} is such that for any RS scheme
(𝛑,𝐏​[𝛑])\left(\boldsymbol{\pi},\boldsymbol{P}\left[\boldsymbol{\pi}\right]\right), the relative compensation vector 𝐏​[𝛑]\boldsymbol{P}\left[\boldsymbol{\pi}\right] is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pi​[𝝅]=Ii∑j=1n+1Ij,i=1,2,…,n+1.P\_{i}\left[\boldsymbol{\pi}\right]=\frac{I\_{i}}{\sum\_{j=1}^{n+1}I\_{j}},\qquad i=1,2,\ldots,n+1. |  | (54) |

Obviously, 𝐏\boldsymbol{P} satisfies the indifference property ([44](https://arxiv.org/html/2510.19511v1#S4.E44 "In 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")).
The RS scheme (𝛑,𝐏​[𝛑])\left(\boldsymbol{\pi},\boldsymbol{P}\left[\boldsymbol{\pi}\right]\right) is actuarially fair for all participants if and only if
the Conditions ([35](https://arxiv.org/html/2510.19511v1#S4.E35 "In 4.1 Actuarially fair risk-sharing schemes ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) are satisfied. Inspired by the approach proposed
in Denuit and Robert (2025), one can verify that the expected proportions
follow from

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[Pi​[𝝅]]=∑k=1n1k​Pr⁡[Ii=1, ​∑j=1nIj=k],i=1,2,…,n.E\left[P\_{i}\left[\boldsymbol{\pi}\right]\right]=\sum\_{k=1}^{n}\frac{1}{k}\Pr\left[I\_{i}=1,\text{ }\sum\_{j=1}^{n}I\_{j}=k\right],\qquad i=1,2,\ldots,n. |  | (55) |

In case the indicator variables IiI\_{i} of the nn participants are mutually independent, the
expressions ([55](https://arxiv.org/html/2510.19511v1#S4.E55 "In Example 8 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) can be transformed into

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[Pi​[𝝅]]=Pr⁡[Ii=1]​∑k=1n1k​Pr⁡[∑j=1nIj−Ii=k−1]i=1,2,…,n.E\left[P\_{i}\left[\boldsymbol{\pi}\right]\right]=\Pr\left[I\_{i}=1\right]\sum\_{k=1}^{n}\frac{1}{k}\Pr\left[\sum\_{j=1}^{n}I\_{j}-I\_{i}=k-1\right]\qquad i=1,2,\ldots,n. |  | (56) |

In this case, the expectations of the relative compensations Pi​[𝛑]P\_{i}\left[\boldsymbol{\pi}\right] follow from probabilities of events related to sums
of independent Bernoulli random variables. The actuarially fair initial investments of
this RS scheme follow then from Proposition 3 and from ([56](https://arxiv.org/html/2510.19511v1#S4.E56 "In Example 8 ‣ 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")). Notice
that for this RS rule, the actuarially fair initial investments are only
defined up to a positive constant factor.
  
The calculations above can
in a straightforward way be generalized to the case that all fif\_{i} are
positive (not necessary equal) integers, rather than all equally 1. We refer
to Denuit and Robert (2025) for more details on this case. ⊲\lhd

## 5 Compensation-based risk-sharing with a passive administrator

### 5.1 Introducing the passive administrator

Consider an RS scheme (𝝅,𝑷)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with
nn participants and an active administrator as defined above. The time 0
investments of the n+1n+1 agents are summarized in the investment vector
𝝅=(π1,π2,…,πn+1)\boldsymbol{\pi}=\left(\pi\_{1},\pi\_{2},\ldots,\pi\_{n+1}\right), while
the relative compensation vector is given by 𝑷=(P1,P2,…,Pn+1)\boldsymbol{P}=\left(P\_{1},P\_{2},\ldots,P\_{n+1}\right). The compensations are summarized in
the compensation vector 𝑾=(W1,W2,…,Wn+1)\boldsymbol{W}=\left(W\_{1},W\_{2},\ldots,W\_{n+1}\right). The latter vector is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wi=(∑j=1n+1πj)×Pii=1,2,…,n+1.W\_{i}=\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times P\_{i}\qquad i=1,2,\ldots,n+1. |  | (57) |

This set up of a compensation-based RS scheme with an active administrator is
a generalization of the set up in Dhaene and Milevsky (2024), who consider
the RS schemes related to tontine funds, as described in Example 2.

Denuit and Robert (2025) also consider the setting of Dhaene and Milevsky
(2024), but with a passive administrator who does not join the group of
participants in investing. Hence, these authors assume that πn+1=0\pi\_{n+1}=0,
implying that (without any adaptation of the compensations), such an RS scheme
can never be actuarially fair, see Proposition 2. In order to
include the possibility that the RS scheme is actuarialy fair for all
participants, Denuit and Robert (2025) assume that in case no participant
receives a positive compensation, that is, in case ∑j=1nPj=0\sum\_{j=1}^{n}P\_{j}=0, or
equivalently, Pn+1=1P\_{n+1}=1, each participant ii receives back his original
investment. Most papers on tontine funds in the last few years have added this
element to repair expectations and hence, actuarial
fairness. Hereafter, we will generalize this approach considered in Denuit
and Robert (2024), in the same way as we generalized the approach of Dhaene
and Milevsky (2024) in the first part of this paper. That is, we will consider
risk-sharing with a passive administrator for a general class of
compensations, instead of restricting to the tontine fund case of Example
2. Let us start by defining a compensation-based RS scheme with a passive administrator.

###### Definition 6

A compensation-based risk-sharing scheme for a given group of nn participants
and a passive administrator is a pair (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right), where 𝛑=(π1,π2,…,πn+1)\boldsymbol{\pi}=\left(\pi\_{1},\pi\_{2},\ldots,\pi\_{n+1}\right) is the initial investment vector with πn+1=0\pi\_{n+1}=0. Further, 𝐏=(P1,P2,…,Pn,Pn+1)\boldsymbol{P}=\left(P\_{1},P\_{2},\ldots,P\_{n},P\_{n+1}\right) is the relative compensation
vector, that is 𝐏∈ℛn+1\boldsymbol{P}\in\mathcal{R}\_{n+1} defined in ([17](https://arxiv.org/html/2510.19511v1#S2.E17 "In Definition 1 ‣ 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), and where the
compensations attributed to the nn participants follow from the compensation
vector 𝐖=(W1,W2,…,Wn+1)\boldsymbol{W}=\left(W\_{1},W\_{2},\ldots,W\_{n+1}\right),
which is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wi=(∑j=1nπj)×Pi+πi×Pn+1:i=1,2,…,n,W\_{i}=\left(\sum\_{j=1}^{n}\pi\_{j}\right)\times P\_{i}+\pi\_{i}\times P\_{n+1}\qquad:i=1,2,\ldots,n, |  | (58) |

whereas Wn+1=0W\_{n+1}=0.

From this definition, we see that an RS scheme (𝝅,𝑷)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with a passive administrator is one where each
participant ii invests an an amount πi\pi\_{i} and receives a relative compensation
PiP\_{i} of the available fund at time 11, whereas the administrator makes an
investment πn+1=0\pi\_{n+1}=0 and receives a zero-compensation Wn+1=0W\_{n+1}=0 at time
11. Moreover, in case the relative compensations PiP\_{i} of all participants
are 0, or equivalently, Pn+1=1P\_{n+1}=1, every participant receives his original
investment πi\pi\_{i} back. The administrator is ‘passive’ in the sense that
he is not involved in investing and receiving any amount of compensation based on the participant’s initial investments.

In order to be able to clearly distinguish between the ’active’ and the ’passive’ administrator case, see ([57](https://arxiv.org/html/2510.19511v1#S5.E57 "In 5.1 Introducing the passive administrator ‣ 5 Compensation-based risk-sharing with a passive administrator ‣ Compensation-based risk-sharing"))and ([58](https://arxiv.org/html/2510.19511v1#S5.E58 "In Definition 6 ‣ 5.1 Introducing the passive administrator ‣ 5 Compensation-based risk-sharing with a passive administrator ‣ Compensation-based risk-sharing")), hereafter we will sometimes write WiactiveW\_{i}^{\text{active}} or WipassiveW\_{i}^{\text{passive}} instead of WiW\_{i} for the contribution of agent ii.

Taking into account that ∑j=1n+1Pj=1\sum\_{j=1}^{n+1}P\_{j}=1, it is a straightforward
exercise to prove the following full allocation property for a
compensation-based RS scheme with a passive administrator:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1nWi=∑j=1nπj.\sum\_{i=1}^{n}W\_{i}=\sum\_{j=1}^{n}\pi\_{j}. |  | (59) |

This means that the total amount of compensations paid at time 11 is exactly equal
to the fund value at that time. Hereafter, when considering an ‘RS scheme
(𝝅,𝑷)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with a passive
administrator’, we mean a ‘compensation-based RS scheme with a passive administrator’.

###### Example 9

Denuit and Robert (2025) and Dhaene and Milevsky (2024) discuss the
above-mentioned approach with a passive administrator for the setting of
Example 2, that is, in the framework of a tontine fund with πn+1=0\pi\_{n+1}=0. In particular, they
consider the RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with
a passive administrator, where the compensation vector 𝐖\boldsymbol{W} is
defined by ([58](https://arxiv.org/html/2510.19511v1#S5.E58 "In Definition 6 ‣ 5.1 Introducing the passive administrator ‣ 5 Compensation-based risk-sharing with a passive administrator ‣ Compensation-based risk-sharing")), with relative compensation vector 𝐏\boldsymbol{P}
given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pi=fi×Ii∑j=1n+1fj×Ij,i=1,2,…,n+1,P\_{i}=\frac{f\_{i}\times I\_{i}}{\sum\_{j=1}^{n+1}f\_{j}\times I\_{j}},\qquad i=1,2,\ldots,n+1, |  | (60) |

where the protection units fif\_{i} and the indicator variables IiI\_{i} are
defined in Example 2. Dhaene and Milevsky (2024) write the following about
this approach: ‘While the above-mentioned approach (i.e., without an (active)
administrator, and returning back the investments if no participant
receives a positive compensation) resolves the mathematical problem, we
believe that this isn’t why people buy tontines. Indeed, it violates the
spirit of the (historical) tontine in which all rights and ownership benefits
are lost at death. Furthermore, some members may not have any beneficiaries,
leading to yet another unintended redistribution of wealth. In extreme cases,
when there is only one person surviving, this may create a moral hazard. In
other words, and for many reasons, while adding a death benefit refund or
payout ‘solves’ the math, it ‘ruins’ the elegance of the tontine ideal.’ As
far as we are aware, Dhaene and Milevsky (2024) are the first who introduce an
active tontine administrator as both a technical and real-world solution to
some of the above-mentioned issues, instead of artificially adding legacy or
bequest payouts to participants.

### 5.2 Actuarially fair risk-sharing schemes with a passive administrator

Similar to actuarial fairness for an RS scheme with an active administrator,
the RS scheme (𝝅, ​𝑷)\left(\boldsymbol{\pi},\text{ }\boldsymbol{P}\right) with
a passive administrator is said to be actuarially fair for the participants if
the time 11 value of each participant’s initial investment is equal to the
expected value of the compensation he will receive at time 11.

###### Definition 7

The RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with a
passive administrator is actuarially fair for all participants if the following
conditions hold:

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi=E​[Wi],i=1,2,…,n.\pi\_{i}=E\left[W\_{i}\right],\qquad i=1,2,\ldots,n. |  | (61) |

Taking into account that πn+1=Wn+1=0\pi\_{n+1}=W\_{n+1}=0, we find that the RS scheme is always actuarially fair for the passive administrator.

In the next proposition, another characterization is given for the actuarial
fairness of an RS scheme with a passive administrator.

###### Proposition 6

The RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with a
passive administrator is actuarially fair for its nn participants if and only if any of the following conditions is satisfied:

Condition 1: The RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi=(∑j=1nπj)×E​[Pi]+πi×E​[Pn+1],i=1,2,…,n.\pi\_{i}=\left(\sum\_{j=1}^{n}\pi\_{j}\right)\times E\left[P\_{i}\right]+\pi\_{i}\times E[P\_{n+1}],\qquad i=1,2,\ldots,n. |  | (62) |

  

Condition 2: The RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi=(∑j=1nπj)×E​[Pi]Pr⁡[Pn+1=0],i=1,2,…,n.\pi\_{i}=\left(\sum\_{j=1}^{n}\pi\_{j}\right)\times\frac{E\left[P\_{i}\right]}{\Pr\left[P\_{n+1}=0\right]},\qquad i=1,2,\ldots,n. |  | (63) |

Proof: Actuarial fairness for all participants is, by definition, equivalent to Condition
1. Taking into account ([10](https://arxiv.org/html/2510.19511v1#S2.E10 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), the actuarial fairness
conditions ([62](https://arxiv.org/html/2510.19511v1#S5.E62 "In Proposition 6 ‣ 5.2 Actuarially fair risk-sharing schemes with a passive administrator ‣ 5 Compensation-based risk-sharing with a passive administrator ‣ Compensation-based risk-sharing")) can be transformed into the expressions
([63](https://arxiv.org/html/2510.19511v1#S5.E63 "In Proposition 6 ‣ 5.2 Actuarially fair risk-sharing schemes with a passive administrator ‣ 5 Compensation-based risk-sharing with a passive administrator ‣ Compensation-based risk-sharing")).

In the following corollary, we show that under appropriate conditions, actuarially fair investments πi\pi\_{i} of the participants in a RS scheme (𝝅,𝑷)(\boldsymbol{\pi},\boldsymbol{P}) with an active administrator are also actuarially fair in the corresponding RS scheme (𝝅,𝑷)(\boldsymbol{\pi},\boldsymbol{P}) with a passive administrator.

###### Corollary 1

Consider an initial investment vector (π1,π2,…,πn)(\pi\_{1},\pi\_{2},\ldots,\pi\_{n}) which is used in both the RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with an active administrator (as defined in ([57](https://arxiv.org/html/2510.19511v1#S5.E57 "In 5.1 Introducing the passive administrator ‣ 5 Compensation-based risk-sharing with a passive administrator ‣ Compensation-based risk-sharing"))(\ref{C100})) and in the RS scheme (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with a passive administrator (as defined in ([58](https://arxiv.org/html/2510.19511v1#S5.E58 "In Definition 6 ‣ 5.1 Introducing the passive administrator ‣ 5 Compensation-based risk-sharing with a passive administrator ‣ Compensation-based risk-sharing"))(\ref{C1a})). Then we have that the following statements are equivalent:

1. (a)

   πi=E​[Wiactive],i=1,2,…,n.\pi\_{i}=E[{W\_{i}^{\text{active}}}],\hskip 5.69054pti=1,2,\ldots,n.
2. (b)

   πi=E​[Wipassive],i=1,2,…,n\pi\_{i}=E[{W\_{i}^{\text{passive}}}],\hskip 5.69054pti=1,2,\ldots,n   and   πn+1=E​[Wn+1active].\pi\_{n+1}=E[W\_{n+1}^{\text{active}}].

Proof: Taking into account Proposition 1 and Condition 2 in Proposition 3, we can rewrite the equations (a)(a) as follows:

|  |  |  |
| --- | --- | --- |
|  | πi=(∑j=1nπj)×E​[Pi]Pr⁡[Pn+1=0],i=1,2,…,n\pi\_{i}=\left(\sum\_{j=1}^{n}\pi\_{j}\right)\times\frac{E[P\_{i}]}{\Pr[P\_{n+1}=0]},\qquad i=1,2,\ldots,n |  |

and

|  |  |  |
| --- | --- | --- |
|  | πn+1=(∑j=1n+1πj)×E​[Pn+1].\pi\_{n+1}=\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times E[P\_{n+1}]. |  |

From Condition 2 in Proposition 6, we can conclude the equations in (a)(a) are equivalent to the equations in (b)(b).

 

Notice that the only if statement of corollary above can also be proven by rewriting ([57](https://arxiv.org/html/2510.19511v1#S5.E57 "In 5.1 Introducing the passive administrator ‣ 5 Compensation-based risk-sharing with a passive administrator ‣ Compensation-based risk-sharing")) and ([58](https://arxiv.org/html/2510.19511v1#S5.E58 "In Definition 6 ‣ 5.1 Introducing the passive administrator ‣ 5 Compensation-based risk-sharing with a passive administrator ‣ Compensation-based risk-sharing")) as

|  |  |  |
| --- | --- | --- |
|  | Wiactive=(∑j=1nπj)×Pi+πn+1×Pi,i=1,2,…,n+1W^{\text{active}}\_{i}=\left(\sum\_{j=1}^{n}\pi\_{j}\right)\times P\_{i}+\pi\_{n+1}\times P\_{i},\qquad i=1,2,\ldots,n+1 |  |

and

|  |  |  |
| --- | --- | --- |
|  | Wipassive=(∑j=1nπj)×Pi+πi×Pn+1,i=1,2,…,n.W^{\text{passive}}\_{i}=\left(\sum\_{j=1}^{n}\pi\_{j}\right)\times P\_{i}+\pi\_{i}\times P\_{n+1},\qquad i=1,2,\ldots,n. |  |

When the participants’ contributions are actuarially fair in case of an active administrator, then from Condition 3 of Proposition 3, we have that

|  |  |  |
| --- | --- | --- |
|  | πn+1×E​[Pi]=πi×E​[Pn+1],i=1,…,n+1.\pi\_{n+1}\times E[P\_{i}]=\pi\_{i}\times E[P\_{n+1}],\qquad i=1,\ldots,n+1. |  |

This implies that

|  |  |  |
| --- | --- | --- |
|  | E​[Wiactive]=E​[Wipassive],i=1,…,n,E[W^{\text{active}}\_{i}]=E[W^{\text{passive}}\_{i}],\qquad i=1,\ldots,n, |  |

which proves the stated implication.

Suppose that the participants in an RS scheme decide to first fix their initial investments and only afterwards make the choice between an active or a passive administrator. Corollary 1 states that from an actuarial fairness point of view, both schemes are equivalent, provided the active administrator makes an actuarially fair initial investment.

### 5.3 Risk-sharing rules with a passive administrator

Similar to section 4.2, where we considered RS rules with an active administrator, we introduce RS rules with a passive administrator. An RS rule 𝑷\boldsymbol{P} with a passive administrator transforms any investment vector 𝝅\boldsymbol{\pi} into a relative compensation vector 𝑷​[𝝅]\boldsymbol{P}[\boldsymbol{\pi}]. This means that any investment vector leads to the compensation vector 𝑾​[𝝅]\boldsymbol{W}[\boldsymbol{\pi}], with

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wi​[𝝅]=(∑j=1nπj)×Pi​[𝝅]+πi×Pn+1​[𝝅],i=1,2,…,n.W\_{i}[\boldsymbol{\pi}]=\left(\sum\_{j=1}^{n}\pi\_{j}\right)\times P\_{i}\left[\boldsymbol{\pi}\right]+\pi\_{i}\times P\_{n+1}\left[\boldsymbol{\pi}\right],\qquad i=1,2,\ldots,n. |  | (64) |

As before, we consider the indifference property ([44](https://arxiv.org/html/2510.19511v1#S4.E44 "In 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) for RS rules with a passive administrator.
It is then a straightforward exercise to prove that Propositions 4 and 5 can easily be adapted to hold for RS rules with a passive administrator.
This means that for RS rules with a passive administrator, which satisfy the indifference property ([44](https://arxiv.org/html/2510.19511v1#S4.E44 "In 4.2 Risk-sharing rules and actuarial fairness ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), actuarially fair investment vectors are only defined up to a positive constant factor.

## 6 The two participants tontine fund

In this section, we investigate an RS scheme related to a tontine fund with
only two participants. We consider both cases of an active and a passive
administrator. We investigate actuarial fairness conditions for the heterogeneous case
where survival probabilities of the two participants may be different.

### 6.1 The two participants tontine fund with an active administrator

Consider two participants who set up a
tontine fund. The initial investment made by participant ii, i=1,2,i=1,2, is
denoted by πi\pi\_{i}, while his survival probability is given by
pi=1−qip\_{i}=1-q\_{i}. In addition to the two participants, also a third agent,
called the active administrator, is involved. His contribution to the
investment pool is denoted by π3\pi\_{3}. As before, for simplicity, we assume a
zero return over the observation period.

Suppose that the participants agree on an RS rule with an active administrator, with relative compensation vector as described in Example 2, that is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pi=fi×Ii∑j=13fj×Ii,i=1,2,3,P\_{i}=\frac{f\_{i}\times I\_{i}}{\sum\_{j=1}^{3}f\_{j}\times I\_{i}},\qquad i=1,2,3, |  | (65) |

and compensations determined from

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wi=(π1+π2+π3)×Pi,i=1,2,3.W\_{i}=\left(\pi\_{1}+\pi\_{2}+\pi\_{3}\right)\times P\_{i},\qquad i=1,2,3. |  | (66) |

The protection units fif\_{i} and the indicator variables IiI\_{i} are as
defined in Example 4. In particular, we have that IiI\_{i} is equal to 11 in
case participant i=1,2i=1,2 survives, while it is equal to 0 otherwise. Furthermore,
I3I\_{3} is equal to (1−I1)×(1−I2)\left(1-I\_{1}\right)\times\left(1-I\_{2}\right).

The relative compensation vector 𝑷=(P1,P2,P3)\boldsymbol{P}=\left(P\_{1},P\_{2},P\_{3}\right) of the RS scheme (𝝅,𝑷)\left(\boldsymbol{\pi},\boldsymbol{P}\right) defined by ([65](https://arxiv.org/html/2510.19511v1#S6.E65 "In 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")) is assumed to be independent of the initial
investments in the sense that the fif\_{i}’s are given real numbers, independent of πi\pi\_{i}. This vector can be expressed as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑷={(1,0,0):if ​I1=1​ and ​I2=0(0,1,0):if ​I1=0​ and ​I2=1(0,0,1):if ​I1=0​ and ​I2=0(β,1−β,0):if ​I1=1​ and ​I2=1\boldsymbol{P}=\left\{\begin{array}[c]{cc}\left(1,0,0\right)&:\text{if }I\_{1}=1\text{ and }I\_{2}=0\\ \left(0,1,0\right)&:\text{if }I\_{1}=0\text{ and }I\_{2}=1\\ \left(0,0,1\right)&:\text{if }I\_{1}=0\text{ and }I\_{2}=0\\ \left(\beta,1-\beta,0\right)&:\text{if }I\_{1}=1\text{ and }I\_{2}=1\end{array}\right. |  | (67) |

with β\beta given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | β=f1f1+f2.\beta=\frac{f\_{1}}{f\_{1}+f\_{2}}. |  | (68) |

If participant 1 survives and participant 2 dies, the total amount of (π1+π2+π3)\left(\pi\_{1}+\pi\_{2}+\pi\_{3}\right) is awarded to person 1 at time 11.
Similarly, if participant 1 dies while participant 2 survives, the total
amount is awarded to person 2 at time 11. If no participant survives, the
total proceeds (π1+π2+π3)\left(\pi\_{1}+\pi\_{2}+\pi\_{3}\right) belong to the
administrator. If both participants survive, (π1+π2+π3)\left(\pi\_{1}+\pi\_{2}+\pi\_{3}\right) is shared by the two participants: The first participant takes
a relative share β\beta of the available funds, while the second participant
receives a relative share (1−β)\left(1-\beta\right) of these funds.

When setting up the tontine RS scheme, the two participants and the
administrator must agree on the value of the relative share β\beta of the
total fund that participant 11 will receive if both participants survive, as
well as on the investments π1\pi\_{1}, π2\pi\_{2} and π3\pi\_{3}. Given the
relative share β\beta, the choice of the initial investments by the
participants may reflect considerations about their survival
probabilities. Consider, for example, uniform risk-sharing, that is β=12\beta=\frac{1}{2} or,
equivalently, f1=f2f\_{1}=f\_{2}, then equal investments may be considered as
‘unfair’ as this choice does not take into consideration that health (survival
probabilities) may be different for both participants. However, notice that
once the relative share β\beta and the investments are chosen, knowledge of
the survival probabilities is no longer required to be able to further manage
the tontine fund.

We assume that the remaining lifetimes of the two participants are mutually
independent. The probabilities of the different relevant events related to
the tontine fund payouts can then be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pr⁡[I1=i​ and ​I2=j]={p1×q2:if ​i=1​ and ​j=0q1×p2:if ​i=0​ and ​j=1q1×q2:if ​i=0​ and ​j=0p1×p2:if ​i=1​ and ​j=1.\Pr\left[I\_{1}=i\text{ and }I\_{2}=j\right]=\left\{\begin{array}[c]{cc}p\_{1}\times q\_{2}&:\text{if }i=1\text{ and }j=0\\ q\_{1}\times p\_{2}&:\text{if }i=0\text{ and }j=1\\ q\_{1}\times q\_{2}&:\text{if }i=0\text{ and }j=0\\ p\_{1}\times p\_{2}&:\text{if }i=1\text{ and }j=1.\end{array}\right. |  | (69) |

In this subsection, we want to find out what is a
reasonable choice for the investments π1\pi\_{1}, π2\pi\_{2} and π3\pi\_{3}, once
the relative share β\beta is chosen. Remark that in case ‘reasonability’ is
translated into ‘actuarial fairness’, the participants have to agree on a common
choice for the survival probabilities p1p\_{1} and p2p\_{2} to determine the
compensations (also called the tontine fund payouts) WiW\_{i}.

Taking into account ([67](https://arxiv.org/html/2510.19511v1#S6.E67 "In 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")) and ([69](https://arxiv.org/html/2510.19511v1#S6.E69 "In 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")), we find that the expected
relative compensations E​[Pi]E\left[P\_{i}\right] of the participants are given
by

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[P1]=p1×(q2+β×p2)E\left[P\_{1}\right]=p\_{1}\times\left(q\_{2}+\beta\times p\_{2}\right) |  | (70) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[P2]=p2×(q1+(1−β)×p1),E\left[P\_{2}\right]=p\_{2}\times\left(q\_{1}+\left(1-\beta\right)\times p\_{1}\right), |  | (71) |

while the administrator’s expected relative compensation E​[P3]E\left[P\_{3}\right] is given by

|  |  |  |
| --- | --- | --- |
|  | E​[P3]=q1×q2.E\left[P\_{3}\right]=q\_{1}\times q\_{2}. |  |

Let us now determine the actuarially fair investments π1,π2\pi\_{1},\pi\_{2} and π3\pi\_{3} for the three participants. From ([38](https://arxiv.org/html/2510.19511v1#S4.E38 "In Proposition 3 ‣ 4.1 Actuarially fair risk-sharing schemes ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), we find that the actuarial
fairness conditions, which state that each agent’s investment is equal to his
expected compensation, are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | {π1=(π1+π2+π3)×p1×(q2+β×p2)π2=(π1+π2+π3)×p2×(q1+(1−β)×p1)π3=(π1+π2+π3)×q1×q2.\left\{\begin{array}[c]{lll}\pi\_{1}&=&\left(\pi\_{1}+\pi\_{2}+\pi\_{3}\right)\times p\_{1}\times\left(q\_{2}+\beta\times p\_{2}\right)\\ \pi\_{2}&=&\left(\pi\_{1}+\pi\_{2}+\pi\_{3}\right)\times p\_{2}\times\left(q\_{1}+\left(1-\beta\right)\times p\_{1}\right)\\ \pi\_{3}&=&\left(\pi\_{1}+\pi\_{2}+\pi\_{3}\right)\times q\_{1}\times q\_{2}.\end{array}\right. |  | (72) |

Any solution (π1,π2,π3)\left(\pi\_{1},\pi\_{2},\pi\_{3}\right) of ([72](https://arxiv.org/html/2510.19511v1#S6.E72 "In 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")) is a set of actuarially fair initial
investments. Determining such a set of investments requires a common choice
for the survival probabilities of the two participants. Important to note is that
even if a ‘wrong’ choice (for instance a too conservative choice) is made,
there will not be an issue of insolvency, due to the full allocation condition
([19](https://arxiv.org/html/2510.19511v1#S2.E19 "In 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), which guarantees that the sum of all tontine fund payouts
(compensations) is exactly equal to the available funds.

Taking into account ([39](https://arxiv.org/html/2510.19511v1#S4.E39 "In Proposition 3 ‣ 4.1 Actuarially fair risk-sharing schemes ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")) and the fact that Pr⁡[P3=0]=1−q1×q2\Pr\left[P\_{3}=0\right]=1-q\_{1}\times q\_{2}, we can rewrite the actuarial fairness conditions
([72](https://arxiv.org/html/2510.19511v1#S6.E72 "In 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {π1=(π1+π2)×p1×q2+β×p21−q1×q2π2=(π1+π2)×p2×q1+(1−β)×p11−q1×q2π3=(π1+π2)×q1×q21−q1×q2\left\{\begin{array}[c]{lll}\pi\_{1}&=&\left(\pi\_{1}+\pi\_{2}\right)\times p\_{1}\times\frac{q\_{2}+\beta\times p\_{2}}{1-q\_{1}\times q\_{2}}\\ \pi\_{2}&=&\left(\pi\_{1}+\pi\_{2}\right)\times p\_{2}\times\frac{q\_{1}+\left(1-\beta\right)\times p\_{1}}{1-q\_{1}\times q\_{2}}\\ \pi\_{3}&=&\left(\pi\_{1}+\pi\_{2}\right)\times\frac{q\_{1}\times q\_{2}}{1-q\_{1}\times q\_{2}}\end{array}\right. |  | (73) |

From ([40](https://arxiv.org/html/2510.19511v1#S4.E40 "In Proposition 3 ‣ 4.1 Actuarially fair risk-sharing schemes ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), we find that the actuarially fairness conditions
can also be expressed as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {π1=π3×p1×q2+β×p2q1×q2π2=π3×p2×q1+(1−β)×p1q1×q2\left\{\begin{array}[c]{l}\pi\_{1}=\pi\_{3}\times p\_{1}\times\frac{q\_{2}+\beta\times p\_{2}}{q\_{1}\times q\_{2}}\\ \pi\_{2}=\pi\_{3}\times p\_{2}\times\frac{q\_{1}+\left(1-\beta\right)\times p\_{1}}{q\_{1}\times q\_{2}}\end{array}\right. |  | (74) |

The formulas ([72](https://arxiv.org/html/2510.19511v1#S6.E72 "In 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")), ([73](https://arxiv.org/html/2510.19511v1#S6.E73 "In 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")) and ([74](https://arxiv.org/html/2510.19511v1#S6.E74 "In 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")) provide 3 different ways
to determine actuarially fair initial investments, once there is an agreement on
the relative share β\beta and the survival probabilities pip\_{i}. One can
first choose the aggregate investments (π1+π2+π3)\left(\pi\_{1}+\pi\_{2}+\pi\_{3}\right) of all participants, or the total investments (π1+π2)\left(\pi\_{1}+\pi\_{2}\right) of all participants, or the investment π3\pi\_{3} of the
administrator, and then use either ([72](https://arxiv.org/html/2510.19511v1#S6.E72 "In 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")), ([73](https://arxiv.org/html/2510.19511v1#S6.E73 "In 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")) or ([74](https://arxiv.org/html/2510.19511v1#S6.E74 "In 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")) to
derive the actuarially fair investments for the 3 participants.

###### Example 10

(A game of chance with a coin and a die) Consider the combined game
of chance with two participants, described in the online appendix of Dhaene and
Milvesky (2024). To enter the game, participant 1 pays an amount π1\pi\_{1},
while participant 2 pays π2\pi\_{2}. Participant 1 tosses a two-sided coin,
while participant 2 rolls a six-sided die. In this game, participant 1 is
successful if he tosses heads, while participant 2 is successful if he rolls a
1. In addition to the two participants, an active administrator is involved.
He contributes to the prize pool by paying an amount π3\pi\_{3}.
  
The
payouts for this game of chance are defined as follows: If the coin lands on
heads and the die does not land on 1, the total amount of (π1+π2+π3)\left(\pi\_{1}+\pi\_{2}+\pi\_{3}\right) is awarded to participant 1. Similarly,
if the coin does not land on heads but the die lands on 1, the total amount of
(π1+π2+π3)\left(\pi\_{1}+\pi\_{2}+\pi\_{3}\right) is awarded to participant 2. If both participants are successful (i.e., heads and 1 appear after the
respective throws), the total proceeds of (π1+π2+π3)\left(\pi\_{1}+\pi\_{2}+\pi\_{3}\right) are shared by person 1 and person 2. In this case, participant
1 receives a relative share β\beta, while participant 2 receives a relative
share (1−β)\left(1-\beta\right) of the available fund. Finally, if both
participants are not successful (i.e., neither heads nor 1 appear after their
respective throws), the total proceeds of (π1+π2+π3)\left(\pi\_{1}+\pi\_{2}+\pi\_{3}\right) go to the administrator. Let us assume that the outcomes of the
coin and the die are independent. The probability that the administrator
will receive the entire prize pool is then given by 512\frac{5}{12}, so it
seems reasonable to require the administrator to contribute to the prize pool
for his chance of winning.

This game of chance can be described
within the framework of the two participants tontine fund considered above in
this subsection:

|  |  |  |
| --- | --- | --- |
|  | Wi=(π1+π2+π3)×Pii=1,2,3,W\_{i}=\left(\pi\_{1}+\pi\_{2}+\pi\_{3}\right)\times P\_{i}\qquad i=1,2,3, |  |

with the relative compensations PiP\_{i} defined by ([67](https://arxiv.org/html/2510.19511v1#S6.E67 "In 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")).
  
From
([72](https://arxiv.org/html/2510.19511v1#S6.E72 "In 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")), we find that the game of chance is actuarially fair for the 3
participants if and only if the amounts π1,π2\pi\_{1},\pi\_{2} and π3\pi\_{3} satisfy the
following set of equations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {π1=(π1+π2+π3)×5+β12π2=(π1+π2+π3)×2−β12π3=(π1+π2+π3)×512\left\{\begin{array}[c]{lll}\pi\_{1}&=&\left(\pi\_{1}+\pi\_{2}+\pi\_{3}\right)\times\frac{5+\beta}{12}\\ \pi\_{2}&=&\left(\pi\_{1}+\pi\_{2}+\pi\_{3}\right)\times\frac{2-\beta}{12}\\ \pi\_{3}&=&\left(\pi\_{1}+\pi\_{2}+\pi\_{3}\right)\times\frac{5}{12}\end{array}\right. |  | (75) |

In this case, the actuarially fair initial investments π1,π2\pi\_{1},\pi\_{2} and
π3\pi\_{3}\ are expressed as proportions of the total payment (π1+π2+π3)\left(\pi\_{1}+\pi\_{2}+\pi\_{3}\right) of the three participants. One can choose the
magnitude of (π1+π2+π3)\left(\pi\_{1}+\pi\_{2}+\pi\_{3}\right) first, and then
determine the corresponding actuarially fair initial payments of the
participants and the administrator by ([75](https://arxiv.org/html/2510.19511v1#S6.E75 "In Example 10 ‣ 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")).
  
From
([73](https://arxiv.org/html/2510.19511v1#S6.E73 "In 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")), we find that the actuarially fairness conditions can also be
expressed in the following way:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {π1=(π1+π2)×5+β7π2=(π1+π2)×2−β7π3=(π1+π2)×57\left\{\begin{array}[c]{lll}\pi\_{1}&=&\left(\pi\_{1}+\pi\_{2}\right)\times\frac{5+\beta}{7}\\ \pi\_{2}&=&\left(\pi\_{1}+\pi\_{2}\right)\times\frac{2-\beta}{7}\\ \pi\_{3}&=&\left(\pi\_{1}+\pi\_{2}\right)\times\frac{5}{7}\end{array}\right. |  | (76) |

In this case, the actuarially fair investments π1,π2\pi\_{1},\pi\_{2} and π3\pi\_{3}\ are
expressed as proportions of the total payment (π1+π2)\left(\pi\_{1}+\pi\_{2}\right) of the two participants. One can choose the magnitude of (π1+π2)\left(\pi\_{1}+\pi\_{2}\right) first , and then determine the corresponding initial
payments of the participants and the administrator by ([76](https://arxiv.org/html/2510.19511v1#S6.E76 "In Example 10 ‣ 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")). Alternatively, one can first choose π1\pi\_{1} and π2\pi\_{2}, and then
determine π3\pi\_{3} and set β\beta equal to 2​π1−5​π2π1+π2\frac{2\pi\_{1}-5\pi\_{2}}{\pi\_{1}+\pi\_{2}}, such that the game is actuarially fair for all participants.
However, notice that in this case, not every choice of π1\pi\_{1} and π2\pi\_{2}
will lead to a relative share β\beta between 0 and 11.
  
Finally,
from ([74](https://arxiv.org/html/2510.19511v1#S6.E74 "In 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")) one finds that the actuarially fair initial investments also follow from

|  |  |  |  |
| --- | --- | --- | --- |
|  | {π1=π3×5+β5π2=π3×2−β5\left\{\begin{array}[c]{c}\pi\_{1}=\pi\_{3}\times\frac{5+\beta}{5}\\ \pi\_{2}=\pi\_{3}\times\frac{2-\beta}{5}\end{array}\right. |  | (77) |

Here, π1\pi\_{1} and π2\pi\_{2} are expressed as proportions of the investment
π3\pi\_{3} of the administrator. One can choose the magnitude of π3\pi\_{3}
first, and then determine the investments of the two participants by
([77](https://arxiv.org/html/2510.19511v1#S6.E77 "In Example 10 ‣ 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")). ⊲\lhd

### 6.2 The two participants tontine fund with a passive administrator

Let us now replace the tontine RS scheme with an active administrator
defined in the previous subsection by the tontine RS scheme (𝝅,𝑷)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with a passive administrator, as
explained before. The investment vector and the compensation vector are now
given by 𝝅=(π1,π2,0)\boldsymbol{\pi}=\left(\pi\_{1},\pi\_{2},0\right) and
𝑾=(W1,W2,0)\boldsymbol{W}=\left(W\_{1},W\_{2},0\right). From ([58](https://arxiv.org/html/2510.19511v1#S5.E58 "In Definition 6 ‣ 5.1 Introducing the passive administrator ‣ 5 Compensation-based risk-sharing with a passive administrator ‣ Compensation-based risk-sharing")), it follows
that the compensations WiW\_{i} of the participants are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wi=(π1+π2)×Pi+πi×P3,i=1,2,W\_{i}=\left(\pi\_{1}+\pi\_{2}\right)\times P\_{i}+\pi\_{i}\times P\_{3},\qquad i=1,2, |  | (78) |

with the relative compensation vector 𝑷=(P1,P2,P3)\boldsymbol{P}=\left(P\_{1},P\_{2},P\_{3}\right) given by ([67](https://arxiv.org/html/2510.19511v1#S6.E67 "In 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")).

From ([63](https://arxiv.org/html/2510.19511v1#S5.E63 "In Proposition 6 ‣ 5.2 Actuarially fair risk-sharing schemes with a passive administrator ‣ 5 Compensation-based risk-sharing with a passive administrator ‣ Compensation-based risk-sharing")), we find that the actuarial fairness conditions for the two
participants are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | {π1=(π1+π2)×p1×(q2+β×p2)1−q1×q2π2=(π1+π2)×p2×(q1+(1−β)×p1)1−q1×q2\left\{\begin{array}[c]{lll}\pi\_{1}&=&\left(\pi\_{1}+\pi\_{2}\right)\times\frac{p\_{1}\times\left(q\_{2}+\beta\times p\_{2}\right)}{1-q\_{1}\times q\_{2}}\\ \pi\_{2}&=&\left(\pi\_{1}+\pi\_{2}\right)\times\frac{p\_{2}\times\left(q\_{1}+\left(1-\beta\right)\times p\_{1}\right)}{1-q\_{1}\times q\_{2}}\end{array}\right. |  | (79) |

Expressions ([79](https://arxiv.org/html/2510.19511v1#S6.E79 "In 6.2 The two participants tontine fund with a passive administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")) provide a way to determine actuarially fair initial
investments for the two participants tontine fund with a passive
administrator. Indeed, once there is an agreement on the relative share
β\beta and the survival probabilities pip\_{i}, one can first choose the
aggregate initial payments (π1+π2)\left(\pi\_{1}+\pi\_{2}\right) of the two
participants, and then use ([79](https://arxiv.org/html/2510.19511v1#S6.E79 "In 6.2 The two participants tontine fund with a passive administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")) to derive actuarially fair investments
πi\pi\_{i}. Another possibility consists of first choosing π1\pi\_{1}, and then
determining π2\pi\_{2} from ([79](https://arxiv.org/html/2510.19511v1#S6.E79 "In 6.2 The two participants tontine fund with a passive administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | π2=π1×p2×(q1+(1−β)×p1)p1×(q2+β×p2).\pi\_{2}=\pi\_{1}\times\frac{p\_{2}\times\left(q\_{1}+\left(1-\beta\right)\times p\_{1}\right)}{p\_{1}\times\left(q\_{2}+\beta\times p\_{2}\right)}. |  | (80) |

###### Example 11

(A game of chance with a coin and a die) Let us revisit the ‘coin
and die’ game of chance with active administrator considered in Example
[10](https://arxiv.org/html/2510.19511v1#Thmexample10 "Example 10 ‣ 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing"). We replace this game of chance with one with a passive administrator and
denote it by (𝛑,𝐏)\left(\boldsymbol{\pi},\boldsymbol{P}\right). From
([6](https://arxiv.org/html/2510.19511v1#Thmdefinition6 "Definition 6 ‣ 5.1 Introducing the passive administrator ‣ 5 Compensation-based risk-sharing with a passive administrator ‣ Compensation-based risk-sharing")), we have that the payouts (compensations) of the transformed RS
scheme are given by ([58](https://arxiv.org/html/2510.19511v1#S5.E58 "In Definition 6 ‣ 5.1 Introducing the passive administrator ‣ 5 Compensation-based risk-sharing with a passive administrator ‣ Compensation-based risk-sharing")) with the relative compensation vector
𝐏\mathbf{P} defined by ([67](https://arxiv.org/html/2510.19511v1#S6.E67 "In 6.1 The two participants tontine fund with an active administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")).
  
From ([79](https://arxiv.org/html/2510.19511v1#S6.E79 "In 6.2 The two participants tontine fund with a passive administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")), we find that
this game of chance is actuarially fair for all its participants if and only if the
initial investments π1\pi\_{1} and π2\pi\_{2} follow from the following set of
equations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {π1=(π1+π2)×5+β7π2=(π1+π2)×2−β7.\left\{\begin{array}[c]{lll}\pi\_{1}&=&\left(\pi\_{1}+\pi\_{2}\right)\times\frac{5+\beta}{7}\\ \pi\_{2}&=&\left(\pi\_{1}+\pi\_{2}\right)\times\frac{2-\beta}{7}.\end{array}\right. |  | (81) |

This set of equations expresses the actuarially fair payments π1\pi\_{1} and
π2\pi\_{2}\ as a proportion of the total investment (π1+π2)\left(\pi\_{1}+\pi\_{2}\right) of the two participants. One can choose the magnitude of
(π1+π2)\left(\pi\_{1}+\pi\_{2}\right) first and then determine the investment
efforts of the participants by ([81](https://arxiv.org/html/2510.19511v1#S6.E81 "In Example 11 ‣ 6.2 The two participants tontine fund with a passive administrator ‣ 6 The two participants tontine fund ‣ Compensation-based risk-sharing")). Alternatively, one can also
first choose π1\pi\_{1} and π2\pi\_{2}, and then set β\beta equal to
2​π1−5​π2π1+π2\frac{2\pi\_{1}-5\pi\_{2}}{\pi\_{1}+\pi\_{2}}, so that the game is actuarial
fair. However, notice that in this case, not every choice of π1\pi\_{1} and
π2\pi\_{2} will lead to a relative share β\beta between 0 and 11. ⊲\lhd

## 7 The homogeneous tontine fund

### 7.1 The homogenous tontine fund with an active administrator

In this subsection, we investigate a special case of the tontine RS scheme
(𝝅,𝑷)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with an active
administrator, described in Example 2. We consider nn
participants and an active administrator. We assume that all protection
units fif\_{i} are equal to 11. The n+1n+1 agents each invest an initial
amount πi\pi\_{i}. The components of the relative compensation vector are given
by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pi=Ii∑j=1n+1Ij,i=1,2,…,n+1.P\_{i}=\frac{I\_{i}}{\sum\_{j=1}^{n+1}I\_{j}},\qquad i=1,2,\ldots,n+1. |  | (82) |

The compensations WiW\_{i} of the n+1n+1 agents follow then from ([18](https://arxiv.org/html/2510.19511v1#S2.E18 "In Definition 2 ‣ 2 Compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")). We consider a homogeneous tontine RS scheme, which means that we assume
that the indicator variables IiI\_{i} of the nn participants are i.i.d, with
Pr⁡[Ii=1]=p=1−q\Pr\left[I\_{i}=1\right]=p=1-q.

Due to symmetry reasons, we must have that E​[Pi]E\left[P\_{i}\right] is equal
for all nn participants. Furthermore, we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[Pn+1]=Pr⁡[In+1=1]=qn.E\left[P\_{n+1}\right]=\Pr\left[I\_{n+1}=1\right]=q^{n}. |  | (83) |

Taking into account that ∑i=1n+1E​[Pi]=1\sum\_{i=1}^{n+1}E\left[P\_{i}\right]=1 leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[Pi]=E​[Ii∑j=1n+1Ij]=1−qnn,i=1,2,…,n.E\left[P\_{i}\right]=E\left[\frac{I\_{i}}{\sum\_{j=1}^{n+1}I\_{j}}\right]=\frac{1-q^{n}}{n},\qquad i=1,2,\ldots,n. |  | (84) |

According to ([39](https://arxiv.org/html/2510.19511v1#S4.E39 "In Proposition 3 ‣ 4.1 Actuarially fair risk-sharing schemes ‣ 4 Actuarial fairness of compensation-based risk-sharing with an active administrator ‣ Compensation-based risk-sharing")), the homogeneous tontine RS scheme (𝝅,𝑷)\left(\boldsymbol{\pi},\boldsymbol{P}\right) is actuarially fair for all agents if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi=1n​∑j=1nπj,i=1,2,…,n\pi\_{i}=\frac{1}{n}\sum\_{j=1}^{n}\pi\_{j},\qquad i=1,2,\ldots,n |  | (85) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | πn+1=qn1−qn​∑j=1nπj.\pi\_{n+1}=\frac{q^{n}}{1-q^{n}}\sum\_{j=1}^{n}\pi\_{j}. |  | (86) |

This implies that all initial investments πi\pi\_{i} of the
participants are equal, which we denote hereafter by π\pi.
This result was to be expected because of the inherent symmetry of the problem. Actuarially fair initial investments can then be determined by first choosing the administrator’s initial investment πn+1\pi\_{n+1} and then determining the participants’ initial investments by ([85](https://arxiv.org/html/2510.19511v1#S7.E85 "In 7.1 The homogenous tontine fund with an active administrator ‣ 7 The homogeneous tontine fund ‣ Compensation-based risk-sharing")) and ([86](https://arxiv.org/html/2510.19511v1#S7.E86 "In 7.1 The homogenous tontine fund with an active administrator ‣ 7 The homogeneous tontine fund ‣ Compensation-based risk-sharing")).

### 7.2 The homogeneous tontine fund with a passive administrator

Let us now replace the homogeneous tontine RS scheme with an active
administrator, considered in Section 7.1, by the corresponding homogeneous
tontine RS scheme (𝝅,𝑷)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with a
passive administrator. The compensations WiW\_{i} are then given by
([58](https://arxiv.org/html/2510.19511v1#S5.E58 "In Definition 6 ‣ 5.1 Introducing the passive administrator ‣ 5 Compensation-based risk-sharing with a passive administrator ‣ Compensation-based risk-sharing")), with the relative compensations PiP\_{i} as defined in
([82](https://arxiv.org/html/2510.19511v1#S7.E82 "In 7.1 The homogenous tontine fund with an active administrator ‣ 7 The homogeneous tontine fund ‣ Compensation-based risk-sharing")).
  
From ([63](https://arxiv.org/html/2510.19511v1#S5.E63 "In Proposition 6 ‣ 5.2 Actuarially fair risk-sharing schemes with a passive administrator ‣ 5 Compensation-based risk-sharing with a passive administrator ‣ Compensation-based risk-sharing")), ([83](https://arxiv.org/html/2510.19511v1#S7.E83 "In 7.1 The homogenous tontine fund with an active administrator ‣ 7 The homogeneous tontine fund ‣ Compensation-based risk-sharing")) and ([84](https://arxiv.org/html/2510.19511v1#S7.E84 "In 7.1 The homogenous tontine fund with an active administrator ‣ 7 The homogeneous tontine fund ‣ Compensation-based risk-sharing")), we find
that (𝝅,𝑷)\left(\boldsymbol{\pi},\boldsymbol{P}\right) is actuarially fair for
its nn participants if and only if all initial investments πi\pi\_{i} of the
participants are all equal:

|  |  |  |
| --- | --- | --- |
|  | πi=1n​∑j=1nπj,i=1,2,…,n.\pi\_{i}=\frac{1}{n}\sum\_{j=1}^{n}\pi\_{j},\qquad i=1,2,\ldots,n. |  |

Again, this result was to be expected because of the inherent symmetry of the problem.

### 7.3 Comparing the homogeneous tontine fund with an active administrator and a centralized insurance approach

Consider a group of nn persons (participants). The one-year survival of
person ii is described by the Bernoulli random variable IiI\_{i}, which equals 11 if he
survives until time 11, while it equals 0 otherwise. The group
is assumed to be homogeneous in the sense that all Bernoulli random variables are i.i.d. with a common survival probability pp. Suppose that each person is willing to invest an initial amount π\pi which will entitle him to a survival benefit at time 11.

The participants could opt for centralized insurance, by each buying
a pure endowment with a premium π\pi. Suppose that the premiums are pure
premiums. In case person ii chooses an insurance with pure premium π\pi,
then, assuming a zero-discount rate, his payout WicW\_{i}^{c} at time 11 is
given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wic=πp×Ii,W\_{i}^{c}=\frac{\pi}{p}\times I\_{i}, |  | (87) |

where we use the superscript ‘cc’ to indicate that this is the payout in a
‘centralized’ approach. The expected payoff in case of buying insurance is
given by

|  |  |  |
| --- | --- | --- |
|  | E​[Wic]=π.E\left[W\_{i}^{c}\right]=\pi. |  |

On average, the premium is equal to the expected insurance payment. This
means that the insurance approach is actuarially fair for each person.

Instead of buying a pure endowment insurance, the participants could decide to
take part in a homogeneous RS scheme (𝝅,𝑷)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with an active administrator. Any participant
makes an initial investment π\pi in the tontine fund. The active
administrator’s investment is, as usual, denoted by πn+1\pi\_{n+1}. The initial investment vector is given by 𝝅=(π,π,…,π,πn+1)\boldsymbol{\pi}=\left(\pi,\pi,\ldots,\pi,\pi\_{n+1}\right). Suppose that the relative compensation vector 𝑷\boldsymbol{P} of the homogeneous RS scheme is
given by ([82](https://arxiv.org/html/2510.19511v1#S7.E82 "In 7.1 The homogenous tontine fund with an active administrator ‣ 7 The homogeneous tontine fund ‣ Compensation-based risk-sharing")). The compensation Wi​(n)W\_{i}(n) that participant ii will receive at time 11 in a fund with nn participants in a decentralized approach with an active administrator is then given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wi​(n)=(n×π+πn+1)×Ii∑j=1n+1Ij,i=1,2,…,n+1,W\_{i}(n)=\left(n\times\pi+\pi\_{n+1}\right)\times\frac{I\_{i}}{\sum\_{j=1}^{n+1}I\_{j}},\qquad i=1,2,\ldots,n+1, |  | (88) |

where we added ‘nn’ in the notation Wi​(n)W\_{i}(n) to indicate the number of participants in the RS scheme.

Let us now assume that the RS scheme (𝝅,𝑷)\left(\boldsymbol{\pi},\boldsymbol{P}\right) is actuarially fair for all participants and for the administrator. Then from ([85](https://arxiv.org/html/2510.19511v1#S7.E85 "In 7.1 The homogenous tontine fund with an active administrator ‣ 7 The homogeneous tontine fund ‣ Compensation-based risk-sharing")) and ([86](https://arxiv.org/html/2510.19511v1#S7.E86 "In 7.1 The homogenous tontine fund with an active administrator ‣ 7 The homogeneous tontine fund ‣ Compensation-based risk-sharing")) we find that the compensations Wi​(n)W\_{i}(n) can be written as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wi​(n)=n×π1−qn×Ii∑j=1n+1Ij,i=1,2,…,n+1.W\_{i}(n)=\frac{n\times\pi}{1-q^{n}}\times\frac{I\_{i}}{\sum\_{j=1}^{n+1}I\_{j}},\qquad i=1,2,\ldots,n+1. |  | (89) |

From ([89](https://arxiv.org/html/2510.19511v1#S7.E89 "In 7.3 Comparing the homogeneous tontine fund with an active administrator and a centralized insurance approach ‣ 7 The homogeneous tontine fund ‣ Compensation-based risk-sharing")), one can prove that for any participant we have

|  |  |  |
| --- | --- | --- |
|  | Wi​(n)=π1−qn×Ii1n​∑j=1nIj+1n​∏j=1n(1−Ij)→a.s.πp×Ii.W\_{i}(n)=\frac{\pi}{1-q^{n}}\times\frac{I\_{i}}{\frac{1}{n}\sum\_{j=1}^{n}I\_{j}+\frac{1}{n}\prod\_{j=1}^{n}(1-I\_{j})}\xrightarrow{a.s.}\frac{\pi}{p}\times I\_{i}. |  |

Intuitively, this means that when the number of participants in the homogeneous tontine fund with an active administrator becomes infinitely large, then with probability 11, the contribution of each participant ii becomes equal to the corresponding insurance payment WicW\_{i}^{c}.

Similarly, for the contribution of the administrator we have

|  |  |  |
| --- | --- | --- |
|  | Wn+1​(n)=n×π1−qn×∏j=1n(1−Ij)→a.s.0.W\_{n+1}(n)=\frac{n\times\pi}{1-q^{n}}\times\prod\_{j=1}^{n}(1-I\_{j})\xrightarrow{a.s.}0. |  |

This means that when the number of participants in the homogeneous tontine fund with an active administrator becomes infinitely large, then with probability 11, the contribution of the administrator becomes equal to 0. We can conclude that the homogeneous tontine fund approach with an active administrator converges to the central insurance approach when the number of participants goes to infinity.

### 7.4 Comparing the homogeneous tontine fund with a passive administrator and a centralized insurance approach

Consider again the group of nn persons as described in Section 7.3. Suppose that the participants decide to take part in a homogeneous RS scheme (𝝅,𝑷)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with a passive administrator. Assuming again actuarially fair (and hence equal) contributions, any participant makes an initial investment, denoted by π\pi, in the tontine fund. The initial investment vector is then given by 𝝅=(π,π,…,π,0)\boldsymbol{\pi}=\left(\pi,\pi,\ldots,\pi,0\right). The compensation that participant ii will receive at time 11 in a fund with nn participants in a decentralized approach with a passive administrator then follows from

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wi​(n)=n×π×Ii∑j=1n+1Ij+π×In+1,i=1,2,…,n.W\_{i}(n)=n\times\pi\times\frac{I\_{i}}{\sum\_{j=1}^{n+1}I\_{j}}+\pi\times I\_{n+1},\quad i=1,2,\ldots,n. |  | (90) |

From ([90](https://arxiv.org/html/2510.19511v1#S7.E90 "In 7.4 Comparing the homogeneous tontine fund with a passive administrator and a centralized insurance approach ‣ 7 The homogeneous tontine fund ‣ Compensation-based risk-sharing")), for any participant ii one has that

|  |  |  |
| --- | --- | --- |
|  | Wi​(n)=π×Ii1n​∑j=1nIj+1n​∏j=1n(1−Ij)+π×∏j=1n(1−Ij)→a.s.πp×Ii,W\_{i}(n)=\pi\times\frac{I\_{i}}{\frac{1}{n}\sum\_{j=1}^{n}I\_{j}+\frac{1}{n}\prod\_{j=1}^{n}(1-I\_{j})}+\pi\times\prod\_{j=1}^{n}\left(1-I\_{j}\right)\xrightarrow{a.s.}\frac{\pi}{p}\times I\_{i}, |  |

which means that when the number of participants in the homogeneous tontine fund with a passive administrator becomes infinitely large, then with probability 11, the contribution of participant ii becomes equal to the insurance payment WicW\_{i}^{c}. We can conclude that the tontine fund with a passive administrator also converges to the centralized insurance approach.

## 8 Conclusion

In this paper, we considered compensation-based RS schemes (𝝅,𝑷)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with an active administrator. At
time 0, each participant ii invests an initial amount πi\pi\_{i} in the
fund, while the administrator invests the amount πn+1\pi\_{n+1} in the same
fund. These initial investments are summarized in the investment vector
𝝅=(π1,π2,…,πn+1)\boldsymbol{\pi}=\left(\pi\_{1},\pi\_{2},\ldots,\pi\_{n+1}\right). At time 11,
each participant and also the administrator receives compensation from the
fund, summarized in the compensation vector 𝑾=(W1,W2,…,Wn+1)\boldsymbol{W}=\left(W\_{1},W\_{2},\ldots,W\_{n+1}\right), which is given by

|  |  |  |
| --- | --- | --- |
|  | Wi=(∑j=1n+1πj)×Pii=1,2,…,n+1,W\_{i}=\left(\sum\_{j=1}^{n+1}\pi\_{j}\right)\times P\_{i}\qquad i=1,2,\ldots,n+1, |  |

where 𝑷=(P1,P2,…,Pn+1)\boldsymbol{P}=\left(P\_{1},P\_{2},\ldots,P\_{n+1}\right) is the
relative compensation vector of the RS scheme under consideration. This setup
is a generalization of the setup in Dhaene and Milevsky (2024) and Denuit and
Robert (2024), who consider RS schemes with relative compensation vector given by
([26](https://arxiv.org/html/2510.19511v1#S3.E26 "In Example 2 ‣ 3 Some examples ‣ Compensation-based risk-sharing")) as described in Example 4 on tontine funds.

Apart from the case of an active administrator, we also considered RS schemes
(𝝅,𝑷)\left(\boldsymbol{\pi},\boldsymbol{P}\right) with a passive
administrator. In this case, the investment vector is given by 𝝅=(π1,π2,…,πn,0)\boldsymbol{\pi}=\left(\pi\_{1},\pi\_{2},\ldots,\pi\_{n},0\right), while the relative compensation
vector is given by 𝑾=(W1,W2,…,Wn,0)\boldsymbol{W}=\left(W\_{1},W\_{2},\ldots,W\_{n},0\right), with

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wi=(∑j=1nπj)×Pi+πi×Pn+1i=1,2,…,nW\_{i}=\left(\sum\_{j=1}^{n}\pi\_{j}\right)\times P\_{i}+\pi\_{i}\times P\_{n+1}\qquad i=1,2,\ldots,n |  | (91) |

where 𝑷=(P1,P2,…,Pn+1)\boldsymbol{P}=\left(P\_{1},P\_{2},\ldots,P\_{n+1}\right) is again
the relative compensation vector of the RS scheme under consideration. This setup is a
generalization of the setup in Denuit and Robert (2025), who consider RS
schemes with relative compensation vector given by ([26](https://arxiv.org/html/2510.19511v1#S3.E26 "In Example 2 ‣ 3 Some examples ‣ Compensation-based risk-sharing")) as described in Example 4 on tontine funds.

For both types of compensation-based RS schemes, we derived actuarial fairness
conditions, that is, conditions under which the initial investment of each
agent is equal to the expected compensation he will receive at time 11.

We considered two particular cases of tontine funds in some detail. First,
the two participant tontine fund was investigated. In this case, two participants
decide to set up a tontine fund and share the terminal fund value among the
survivors. We also considered the homogeneous tontine fund, where all
participants have i.i.d. survival indicator variables and purchase equal numbers of protection units. Finally, we also considered the relation between the homogeneous tontine fund approach with passive and active administrators and the centralized insurance approach.

#### Acknowledgments.

Jan Dhaene gracefully acknowledges funding from FWO and F.R.S.-FNRS under the Excellence of Science (EOS) programme, project ASTeRISK (40007517). Atibhav Chaudhry gracefully acknowledges support by an Australian Government Research Training Program (RTP) Scholarship, a Faculty of Business and Economics Doctoral Program Scholarship, a University of Melbourne Research Scholarship, and the 2021 Kilmany Scholarship. Ka Chun Cheung is supported by a grant from the Research Grants Council of the Hong Kong Special Administrative Region, China (Project No. 17303721). Austin Riis-Due gratefully acknowledges the support of The James C. Hickman Scholars Award. The authors also thank Michel Denuit, Runhuan Feng, Zinoviy Landsman, Daniël Linders, Moshe Milevsky and Bertrand Tavin for helpful comments on earlier versions of the paper.

#### Competing interests.

The authors have no competing interests to declare.

## 9 References

* Abdikerimova, S., & Feng, R. (2022). Peer-to-peer multi-risk insurance and mutual aid. European Journal of Operational Research, 299 (2), 735–749.
* Bernard, C., Feliciangeli, M., & Vanduffel, S. (2025). Can an actuarially unfair tontine be optimal? The Geneva Risk and Insurance Review, 50 (1), 39–71.
* Cheung, K. C., & Lo, A. (2014). Characterizing mutual exclusivity as the strongest negative multivariate dependence structure. Insurance: Mathematics and Economics, 55, 180–190.
* Denuit, M., & Dhaene, J. (2012). Convex order and comonotonic conditional mean risk sharing. Insurance: Mathematics and Economics, 51 (2), 265–270.
* Denuit, M., Dhaene, J., Ghossoub, M., & Robert, C. Y. (2025). Comonotonicity and pareto optimality, with application to collaborative insurance. Insurance: Mathematics and Economics, 120, 1–16.
* Denuit, M., Dhaene, J., & Robert, C. Y. (2022). Risk-sharing rules and their properties, with applications to peer-to-peer insurance. Journal of Risk and Insurance, 89 (3), 615–667.
* Denuit, M., & Robert, C. Y. (2023). Endowment contingency funds for mutual aid and public financing. LIDAM Discussion Papers ISBA 2023009, Université catholique de Louvain, Institute of Statistics, Biostatistics and Actuarial Sciences (ISBA).
* Denuit, M., & Robert, C. Y. (2025). Equal compensations under actuarially fair contributions in endowment contingency funds. Risk Sciences, 1, 100005.
* Dhaene, J., & Denuit, M. (1999). The safest dependence structure among risks. Insurance: Mathematics and Economics, 25 (1), 11–21.
* Dhaene, J., Kazzi, R., & Valdez, E. A. (2026). Axiomatic characterizations of some simple risk-sharing rules. Risk Sciences, 2.
* Dhaene, J., & Milevsky, M. A. (2024). Egalitarian pooling and sharing of longevity risk aka can an administrator help skin the tontine cat? Insurance: Mathematics and Economics, 119, 238–250.
* Dhaene, J., Robert, C. Y., Cheung, K. C., & Denuit, M. (2025). An axiomatic characterization of the quantile risk-sharing rule. Scandinavian Actuarial Journal, 1–20.
* Jiao, Z., Kou, S., Liu, Y., & Wang, R. (2022). An axiomatic theory for anonymized risk sharing. arXiv preprint arXiv:2208.07533.
* Lauzier, J.-G., Lin, L., & Wang, R. (2024). Negatively dependent optimal risk sharing. arXiv preprint arXiv:2401.03328.
* Tavin, B. (2023). Reply to request from Dhaene and Milevsky [Private communication]