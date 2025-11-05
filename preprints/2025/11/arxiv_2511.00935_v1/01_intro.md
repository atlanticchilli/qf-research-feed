---
authors:
- Akhil Rao
doc_id: arxiv:2511.00935v1
family_id: arxiv:2511.00935
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Public Infrastructure Investments for Space Market Development
url_abs: http://arxiv.org/abs/2511.00935v1
url_html: https://arxiv.org/html/2511.00935v1
venue: arXiv q-fin
version: 1
year: 2025
---


Akhil Rao
Rational Futures, Washington D.C. Email: akhil@rationalfutures.com.I am grateful to Alex MacDonald, Adrian Mangiuca, Moon Kim, Tom Colvin, Renata Kommel, Elaine Gresham, Carie Mullins, and Cullen Balinski for many helpful discussions and insights. All errors are my own.

###### Abstract

Advanced space technology systems often face high fixed costs, can serve limited non-government demand, and are significantly driven by non-market motivations. While increased entrepreneurial activity and national ambitions in space have encouraged planners at public space agencies to develop markets around such systems, the very factors that make the recent growth of the space economy so remarkable also challenge planners’ efforts to develop and sustain markets for space-related goods and services. I propose a graphical framework to visualize the number of competitors a market can sustain as a function of the industry’s cost structure; the distribution of government support across direct purchases, direct investments, and shared infrastructure; and the magnitude of non-government demand. Building on public goods theory, the framework shows how marginal dollars invested in shared infrastructure can create non-rival benefits supporting more competitors per dollar than direct purchases or subsidies. I demonstrate the framework with a stylized application inspired by NASA’s Commercial LEO Destinations program. Under cost and demand conditions consistent with public data, independent stations generate industry-wide losses of $355 million annually, while shared core infrastructure enables industry-wide profits of $154 million annually. I also outline key directions for future research on public investment and market development strategies for advanced technologies.

> Technology, under all circumstances, leads to planning; in its higher manifestations it may put the problems of planning beyond the reach of the industrial firm. Technological compulsions, and not ideology or political wile, will require the firm to seek the help and protection of the state.
>
> — John Kenneth Galbraith, The New Industrial State

## 1 Introduction

Public space agencies are increasingly interested in developing sustainable markets for advanced space technologies. Several have adopted market development goals, in some cases seeking to transition from direct provision to commercial procurement of space services (NASA, [2019](https://arxiv.org/html/2511.00935v1#bib.bib41); European Commission, [2025](https://arxiv.org/html/2511.00935v1#bib.bib20); ESA, [2025a](https://arxiv.org/html/2511.00935v1#bib.bib18); Cabinet Office, Government of Japan, [2024](https://arxiv.org/html/2511.00935v1#bib.bib5); EY Global, [2024](https://arxiv.org/html/2511.00935v1#bib.bib21)) Yet a basic economic question—how should a public space agency invest in space activities to develop and sustain markets for space-related goods and services—remains underexplored. While systems like the International Space Station (ISS) demonstrate clear technical capabilities—from scientific research across domains as diverse as biology (Castro-Wallace et al., [2017](https://arxiv.org/html/2511.00935v1#bib.bib7)), astronomy (Magalhães et al., [2021](https://arxiv.org/html/2511.00935v1#bib.bib37)), and economics (Henderson et al., [2012](https://arxiv.org/html/2511.00935v1#bib.bib26)) to emerging commercial applications like ZBLAN glass production (Werner, [2024](https://arxiv.org/html/2511.00935v1#bib.bib65))—the transition from government-funded capabilities to competitive markets remains challenging. High fixed costs, long development timelines, and uncertain market demand create conditions where programs to develop and sustain space markets must contend with the risk that the supply side collapses, leaving a monopoly or no market at all. Space technology systems also serve non-market motivations like signaling national achievement or capability (MacDonald, [2017](https://arxiv.org/html/2511.00935v1#bib.bib35)). These goals complicate market development efforts, as market forces alone may not demand sufficiently capable systems.

Space agencies also often have dual objectives: they must procure mission inputs—transportation services, spacecraft components, advanced research facilities—cost-effectively, while also ensuring the continued existence of industrial capabilities that serve limited non-government demand and have high barriers to entry. As space ambitions rise globally while public budgets face greater strain, understanding and clearly communicating principles of pro-competitive public investment in advanced technology systems is an increasingly important task for economists and public space agency officials. In this essay I propose a graphical framework to assist space agency planners in designing advanced technology programs to encourage competition and market development.

The framework enables space agency planners to assess how different distributions of program budgets across direct purchases, direct transfers, and shared infrastructure affect the number of competitors a market can sustain. It supports analysis of what I term “economic architecture.” Just as systems engineering uses “architecture” to describe how technical components fit and work together, a program’s economic architecture determines which and how many technology systems are economically viable. Building on the standard theory of public goods (Samuelson, [1954](https://arxiv.org/html/2511.00935v1#bib.bib55)), the key insight is that marginal dollars invested in shared infrastructure can create non-rival benefits supporting more competitors per dollar than direct purchases or subsidies. By plotting the number of competitors sustainable at different levels of total direct government revenues and industry total costs, the diagram reveals regions where different numbers of firms can earn positive profits, showing precisely when shared infrastructure investments enable competition that direct support mechanisms cannot sustain.

I demonstrate the framework using a stylized application inspired by NASA’s Commercial LEO Destinations program, comparing independent free-flyer versus shared core module architectures for sustaining at least two competing crewed space station operators. Under cost and demand conditions consistent with public data, independent stations generate industry-wide losses of $355 million annually, while shared core infrastructure enables each firm to earn $77 million in annual profits. Scenario analysis reveals how external factors like market demand and interest rates can overwhelm program design choices, underscoring market development programs’ vulnerability to conditions beyond agency control.

This work addresses gaps across three research strands. The public economics literature has explored optimal public-private contracts (Laffont and Tirole, [1993](https://arxiv.org/html/2511.00935v1#bib.bib33); Danau and Vinella, [2015](https://arxiv.org/html/2511.00935v1#bib.bib14)) and developed typologies for space sector partnerships (Kim, [2023](https://arxiv.org/html/2511.00935v1#bib.bib30)), but provides few actionable frameworks for sustaining advanced technology industrial sectors.111Unlike statistical or financial agencies, public space agencies do not usually have internal economic analysis teams that utilize the types of analytical tools developed in the economics literature. NASA’s Chief Economist role was, to my knowledge, one of the few such functions in a public space agency globally (SpaceRef, [2019](https://arxiv.org/html/2511.00935v1#bib.bib57)). This paper is informed by my work with the Chief Economist team within NASA’s Office of Technology, Policy, and Strategy. Among other things, the team developed estimates of non-NASA demand in markets of strategic interest to the agency and assessed economic architectures for existing and proposed programs. All inputs for that demand estimation were derived from publicly available sources. The Chief Economist function was eliminated with the Office of Technology, Policy, and Strategy in early 2025 (Smith, [2025](https://arxiv.org/html/2511.00935v1#bib.bib56)). Techno-economic analyses focus on single system architectures (Proctor et al., [2021](https://arxiv.org/html/2511.00935v1#bib.bib51); Colvin et al., [2020a](https://arxiv.org/html/2511.00935v1#bib.bib9); Metzger, [2023](https://arxiv.org/html/2511.00935v1#bib.bib38)) while remaining silent on competitive dynamics or optimal support mechanisms. “Strategic” demand estimation capabilities for nascent space markets remain underdeveloped, with few such assessments existing beyond those produced by think tanks for specific government sponsors (Crane et al., [2017](https://arxiv.org/html/2511.00935v1#bib.bib11); Colvin et al., [2020b](https://arxiv.org/html/2511.00935v1#bib.bib10); Triezenberg et al., [2020](https://arxiv.org/html/2511.00935v1#bib.bib60); MITRE, [2021](https://arxiv.org/html/2511.00935v1#bib.bib39); Triezenberg et al., [2024](https://arxiv.org/html/2511.00935v1#bib.bib61)).
“Strategic” demand estimates need not be econometrically identified, but must be constructible for nascent or non-existent markets within weeks or months, quantify demand across years or decades to within an order of magnitude, and reflect relevant technical system characteristics and their likely evolutions. By integrating insights across these areas into a simple graphical tool, this framework provides planners at space agencies with a systematic approach to assess program design trade-offs.

The structure of this essay is as follows. In section 2 I describe the general framework for assessing economic architectures of market development programs. This framework is generic, though it is best suited to advanced technology systems with high fixed costs, long development timelines, and highly uncertain market demand. In section 3 I apply the framework to private space stations in low-Earth orbit. In section 4 I identify key directions for future research on public investment and market development strategies for advanced technologies, including improved economic measurement, strategic demand estimation, and better understanding of how private investors perceive different revenue sources. I conclude in section 5.

## 2 A framework for assessing economic architectures of market development programs

Consider a public space agency with annual budget BB designing a program to develop sustainable markets for a class of advanced space technology systems. These systems—such as crewed space stations, lunar surface power systems, or orbital debris removal spacecraft—typically exhibit high fixed costs, long development timelines, and uncertain non-government demand, creating conditions where uncoordinated private investment may result in too few competitors or none at all.222As Weinzierl ([2018](https://arxiv.org/html/2511.00935v1#bib.bib64)) notes, complementarities between space technologies mean space businesses across the technology stack play stag hunts with each other. This framework assumes the public space agency is a planner capable of structuring technological complementarities between private actors to encourage desired outcomes. I refer to the NN firms that develop and utilize the technology systems of interest as “the industry.” I express all economic variables as equivalent annuity units to facilitate comparison across different payment timing structures, assume firms are symmetric in costs and capabilities, and ignore inflation.

The agency can use the program budget to purchase goods and services produced by the industry (RiGR^{G}\_{i} from firm ii), to invest in shared infrastructure for the industry (GSG^{S}), or to directly transfer funds to the industry (GiG\_{i} to firm ii, GD=∑iGiG^{D}=\sum\_{i}G\_{i}).333The specific mechanisms, e.g., loans, grants, preferred shares, etc. are not relevant to the high-level analysis here and introduce additional complexity. Non-dilutive cash grants are a common transfer mechanism and analytically tractable. Ignoring overhead and administrative costs, the program’s budget constraint is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑iRiG+∑iGi+GS≤B.\sum\_{i}R^{G}\_{i}+\sum\_{i}G\_{i}+G^{S}\leq B. |  | (1) |

Public investment into shared infrastructure produces a flow of shared benefits YGY^{G} for the industry according to the production and valuation function f​(GS)f(G^{S}). This function measures the extent to which shared infrastructure reduces firms’ costs relative to developing equivalent capabilities independently. For modular technology systems like space stations, shared infrastructure benefits may be approximately linear up to the cost of shareable essential elements—such as life support systems or power generation—then exhibit sharply diminishing returns thereafter. For network systems requiring interoperability, benefits may show increasing returns to scale as more participants connect to the shared network component. The specific functional form depends on the technology systems and business models involved, and could vary across firms. Here, I assume firms uniformly value shared infrastructure at cost: YG=GSY^{G}=G^{S}.

Firms in the industry earn total revenue RiR\_{i}, with RiGR\_{i}^{G} earned from the program and RiMR^{M}\_{i} earned from “the market.” “The market” captures all sources of demand which are exogenous to the agency—e.g., individuals, households, firms, other public space agencies, and any other public or private entities that may purchase the industry’s output. In specific applications, revenues earned from the agency or the market can be divided between firms according to market share functions σiG​(RG)≡RiG\sigma^{G}\_{i}(R^{G})\equiv R^{G}\_{i} and σiM​(RM)≡RiM\sigma^{M}\_{i}(R^{M})\equiv R^{M}\_{i}. Under symmetry each firm receives an equal share of both government and market revenues, so these simplify to σiG​(RG)=RiG=RG/N\sigma^{G}\_{i}(R^{G})=R^{G}\_{i}=R^{G}/N and σiM​(RM)=RiM=RM/N\sigma^{M}\_{i}(R^{M})=R^{M}\_{i}=R^{M}/N. Similarly, direct transfers are simplified to Gi=GD/NG\_{i}=G^{D}/N.444Allowing for asymmetry introduces additional modeling choices such as the order of entry or exit, quickly exploding the number of possible cases. Institutional knowledge can guide analysts toward particular asymmetric scenarios.

Total industry revenue is R=∑i(RiG+RiM)R=\sum\_{i}(R\_{i}^{G}+R\_{i}^{M}). Firms in the industry incur gross total cost XiX\_{i} and net total cost Ci=Xi−YG−GiC\_{i}=X\_{i}-Y^{G}-G\_{i}, and industry’s total cost is C=∑iCiC=\sum\_{i}C\_{i}. The gross costs XiX\_{i} represent the costs to develop, deploy, and operate the target advanced technology system. Let X=∑iXiX=\sum\_{i}X\_{i} be the industry-level gross total cost. Under symmetry, Xi=X/NX\_{i}=X/N. While these costs must be controlled, it is widely understood by space technology program managers that there is often a positive relationship between a system’s performance and its cost. For example, Section 4.2.1 of NASA’s Cost Estimating Handbook states: “The objective of a cost-performance trade study is not necessarily to minimize the cost of the system, but to achieve an optimal balance of performance and cost” (NASA Executive Cost Analysis Steering Group, [2015](https://arxiv.org/html/2511.00935v1#bib.bib49)). With suitable caveats, then, an advanced technology system’s cost may be used a proxy for its performance during program design.

Assuming the agency exhausts its budget, individual firms’ profits are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Πi\displaystyle\Pi\_{i} | =Ri−Ci\displaystyle=R\_{i}-C\_{i} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =B−GS+RM−XN+f​(GS)\displaystyle=\frac{B-G^{S}+R^{M}-X}{N}+f(G^{S}) |  | (2) |

Agencies intending to promote industry may allocate some of their budget towards increasing industry profits. A marginal dollar provides greater support to the industry if invested in shared infrastructure than if used for direct purchasing when:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀i,∂Πi∂GS\displaystyle\forall i,~\frac{\partial\Pi\_{i}}{\partial G^{S}} | >∂Πi∂RG\displaystyle>\frac{\partial\Pi\_{i}}{\partial R^{G}} |  |

In the symmetric case, this reduces to:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f′​(GS)\displaystyle f^{\prime}(G^{S}) | >1N.\displaystyle>\frac{1}{N}. |  | (3) |

An identical condition holds for direct investment.

If the public space agency wants to maintain at least NN competitors, then it must ensure RGR^{G}, GDG^{D}, and YGY^{G}—its support for the industry—are sufficient to ensure all NN firms earn non-negative profits, conditional on the anticipated level of market demand, RMR^{M}. Formally:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀i,Πi​(N)\displaystyle\forall i,~\Pi\_{i}(N) | ≥0\displaystyle\geq 0 |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟹B−GS+RM−XN+f​(GS)\displaystyle\implies\frac{B-G^{S}+R^{M}-X}{N}+f(G^{S}) | ≥0\displaystyle\geq 0 |  | (4) |

This constraint captures the fundamental trade-off facing market development programs: supporting more competitors requires either reducing individual firm costs (through shared infrastructure investments) or increasing industry revenues (through direct purchases, transfers, or market growth). Programs that violate this constraint will see firms exit, potentially ending in monopoly or no suppliers at all. The agency can use firms’ profitability constraints and its own budget constraint to assess high-level program design trade-offs, particularly how to allocate budget across direct purchases, direct transfers, and shared infrastructure. Questions regarding the timing and conditioning of specific payments or infrastructure access can be investigated by appropriately modeling and discounting the flows of benefits received by the industry when calculating RGR^{G}, GDG^{D}, and YGY^{G}.

The full architectural possibility set can be visualized by taking intersections of industry total costs and government direct purchases where each firm earns non-negative profits at a given industry size, and then overlaying these regions across different industry sizes. For fixed industry size NN, these regions are formally described by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {(RG,C):∀i,Πi​(N)≥0},\displaystyle\{(R^{G},C):~\forall i,~\Pi\_{i}(N)\geq 0\}, |  | (5) |

i.e., intersections of superlevel sets for firms’ profitability constraints under the given assumptions.555Similar diagrams are used in managing engineering costs and schedules in advanced technology programs, e.g., Joint Confidence Level plots (NASA Executive Cost Analysis Steering Group, [2015](https://arxiv.org/html/2511.00935v1#bib.bib49)). The resulting diagram can be used to assess how many competitors can be sustained by different economic architectures under consistent assumptions. Direct government purchases from the industry, RGR^{G}, is the portion of agency support that appears on firms’ income statements. Industry total costs, C=X−YG−GDC=X-Y^{G}-G^{D}, shows the cost burden firms face after accounting for shared infrastructure benefits and direct transfers. Regions where profits are non-negative for a fixed industry size show combinations of total costs and direct purchases that can sustain that many firms. Within these regions, increases in direct purchases can be traded off against reductions in net industry costs to maintain the same expected level of competition.

To make this concrete, suppose a public space agency is considering two alternative economic architectures for a program intended to sustain at least two firms developing and utilizing certain technology systems. In architecture A the agency will directly transfer all funds to the industry as non-dilutive grants, while in architecture B the agency will evenly divide its budget between direct purchases and shared infrastructure. Industry’s expected market revenues are valued at $1B/year (i.e., $0.5B/year/firm), industry gross total costs are $2B/year with two firms in the industry (i.e., $1B/year/firm), and the program has $1B/year to allocate. Suppose also that firms uniformly value the benefits provided by shared infrastructure at cost.666In this example, analysis of condition ([3](https://arxiv.org/html/2511.00935v1#S2.E3 "In 2 A framework for assessing economic architectures of market development programs ‣ Public Infrastructure Investments for Space Market Development")) shows that this assumption implies shared infrastructure better supports the industry than direct purchasing or direct investment at all industry sizes. Table [1](https://arxiv.org/html/2511.00935v1#S2.T1 "Table 1 ‣ 2 A framework for assessing economic architectures of market development programs ‣ Public Infrastructure Investments for Space Market Development") lists the economic parameters for an individual firm under both economic architecture assuming two competitors, with parameter choices selected to illustrate the framework’s key insights about infrastructure versus direct support trade-offs.

I assumed the program intends to sustain at least two firms. As Table [1](https://arxiv.org/html/2511.00935v1#S2.T1 "Table 1 ‣ 2 A framework for assessing economic architectures of market development programs ‣ Public Infrastructure Investments for Space Market Development") shows, under economic architecture A the industry just barely breaks even at the desired size, while under economic architecture B the industry earns positive profits at the desired size. Figure [1](https://arxiv.org/html/2511.00935v1#S2.F1 "Figure 1 ‣ 2 A framework for assessing economic architectures of market development programs ‣ Public Infrastructure Investments for Space Market Development") places the architectures in the program’s sustainable competition diagram, illustrating relevant system cost and government-derived revenue thresholds for different sustainable industry sizes. Note that economic architecture A sits on the boundary between the sustainable duopoly and sustainable monopoly regions, while economic architecture B lies comfortably within the sustainable triopoly region.

Table 1: Economic parameters under alternative program architectures

|  |  |  |
| --- | --- | --- |
|  | Economic architecture A | Economic architecture B |
| Desired number of competitors (NN) | 2 firms | 2 firms |
| Program budget (BB) | $1 B/year | $1 B/year |
| Direct transfers (GiG\_{i}) | $0.5 B/year/firm | — |
| Direct purchases (RiGR^{G}\_{i}) | — | $0.25 B/year/firm |
| Shared infrastructure spending (GSG^{S}) | — | $0.5 B/year |
| Market revenue (RiMR^{M}\_{i}) | $0.5 B/year/firm | $0.5 B/year/firm |
| Shared infrastructure value (YGY^{G}) | — | $0.5 B/year/firm |
| Gross total cost (XiX\_{i}) | $1 B/year/firm | $1 B/year/firm |
| Total industry revenues (RR) | $2 B/year | $1.5 B/year |
| Total industry costs (CC) | $2 B/year | $1 B/year |
| Total industry profits (Π\Pi) | $0 B/year | $0.5 B/year |

![Refer to caption](images/fig1-prod--diagram-demo-unified.png)


Figure 1: Sustainable competition diagram showing the relationship between industry-level direct government purchases, industry-level total costs, and the potential number of profitable firms. Shaded regions indicate the expected sustainable number of competitors under different system cost and government-derived revenues.

Both representations show that under economic architecture A, high-cost shocks or low-market demand shocks are likely to require additional budget outlays to prevent the industry from collapsing to a monopoly. Equivalently, the industry can weather greater uncertainty under economic architecture B than under economic architecture A. In the next section, I develop an application to illustrate how this framework can be used to support program design.

## 3 An application to commercial crewed space stations

Commercial space stations exhibit the high fixed costs, uncertain market demand, and opportunities for shared infrastructure that characterize many advanced space technology systems. Suppose a public space agency with a human spaceflight program intended to maintain continuous human presence in low-Earth orbit while developing sustainable commercial markets for space station services.777“Continuous presence” has been a stated goal of U.S. space policy for some time (NASA, [2024](https://arxiv.org/html/2511.00935v1#bib.bib46)). Such non-economic goals are common in space policy, which is often meant to support a sense of national achievement. MacDonald ([2017](https://arxiv.org/html/2511.00935v1#bib.bib35)) discusses this dimension of space economics in greater detail. Should the agency support multiple independent “free-flyer” stations, each providing complete space station capabilities, or should it invest in shared infrastructure that multiple firms can utilize while developing their own specialized modules? Using cost estimates derived from analogous system elements and budget assumptions consistent with NASA planning, I compare these two approaches to demonstrate the framework’s application to program design decisions.

A program supporting continuous human presence requires substantial investment in both station capabilities and crew operations, with private investors expecting returns over the asset’s full lifetime. I assume the program covers transportation to and from the station as well as crew supplies and equipment. Since transportation and crew support costs remain roughly constant regardless of whether the program supports independent stations or shared infrastructure, the economically relevant comparison focuses on the “capturable budget”—funds available for direct purchases, direct transfers, and shared infrastructure investment. Based on the 2026 NASA President’s Budget Request for commercial space station services, this capturable budget amounts to approximately $1B annually.888The 2026 NASA President’s Budget Request contains roughly $2B for crewed space station services in 2030, when the ISS is retired and private stations become operational (NASA, [2025a](https://arxiv.org/html/2511.00935v1#bib.bib47)). This includes approximately $1.2B for transportation and resupply flights. The remaining $800M represents the capturable portion available for station-related investments, rounded to $1B for analytical convenience. I assume market demand from research institutions, private companies, and other national space agencies and government entities provides an additional $500M annually in total potential revenue for station operators.

The economic architecture choices regarding shared infrastructure stem from the separability of space station functions. Space stations provide two distinct types of capabilities: core functions that every crewed station requires, and habitat functions that differentiate market offerings. Core functions include life support systems capable of sustaining crew between resupply missions, power generation and distribution, command and data handling, and docking capabilities for crew and cargo vehicles. These systems must meet stringent safety and performance requirements regardless of the station’s intended market—a facility serving government researchers needs the same fundamental life support capabilities as one targeting commercial customers.999The Environmental Control and Life Support System (ECLSS) on the ISS currently performs at about 42% O2 recovery from CO2 air loop closure (NASA, [2022](https://arxiv.org/html/2511.00935v1#bib.bib45)). A station aimed at long-duration research missions may require higher recovery rates than one serving short-duration tourists, but both need reliable life support systems. Habitat functions, by contrast, determine what activities crew can perform: research laboratories, manufacturing facilities, recreational amenities, or specialized equipment deployment capabilities. A crewed station operator targeting pharmaceutical research will invest differently in habitat capabilities than one serving space tourism, but both require identical core infrastructure to keep humans alive and connected to Earth. This functional separation creates a natural opportunity for shared infrastructure investment, where the public agency provides essential core capabilities that all operators need, while private firms differentiate their offerings through specialized habitat modules.

Suppose the program supports continuous presence through stations accommodating up to 8 crew members, with government flights carrying up to 2 agency astronauts per flight through two crew rotations annually, leaving at least 2 seats per flight available for other paying customers.101010I am not assuming the government space agency fully fills each flight with its own astronauts, only that the agency pays for the flight. The public space agency may use the seats to barter with other space agencies, to sell back to the public at a discount, or find another use for them. Barter arrangements between space agencies using the ISS are not uncommon (Veldhuyzen and Grifoni, [1999](https://arxiv.org/html/2511.00935v1#bib.bib62); Selding, [2014](https://arxiv.org/html/2511.00935v1#bib.bib16); Foust, [2025](https://arxiv.org/html/2511.00935v1#bib.bib24)). This flight cadence, supported by two dedicated resupply missions annually, ensures substantial station capacity remains available for non-government customers, creating the market opportunity that private investors must evaluate. I assume stations have 15-year design lifetimes with construction beginning in 2025, and that private investors expect 5% annual returns over the asset lifetime.111111Depreciation and maintenance requirements will depend on the system architecture; I assume these are captured in the operating costs. I assume these costs and revenues are fixed in base year terms for the duration of the program. In the independent free-flyer architecture, each firm develops complete station capabilities including both core and habitat functions. In the shared core module architecture, the government provides a common core infrastructure supporting life support, power, docking, and robotic arm capabilities, while private firms develop specialized habitat modules that connect to this shared foundation. In the shared core architecture, I assume the core module can accommodate up to two habitat modules, with government demand for station services split equally between providers in scenarios with multiple competitors. These assumptions are consistent with current NASA use of the ISS and the capabilities of existing crew and cargo vehicles.

To estimate the costs of these two architectures, I derive cost data from comparable space station components currently under development or currently operational. Cost estimates for core module elements come from NASA’s Gateway program, which provides the closest available analogs for long-duration crewed space infrastructure: the Power and Propulsion Element (PPE) contract provides cost data for power and thermal systems, the Habitation and Logistics Outpost (HALO) contract provides data for pressurized volume and life support integration, and the Canadian Space Agency’s (CSA) Canadarm3 contract provides data for robotic capabilities. Habitat module construction costs derive from the European Space Agency’s (ESA) Columbus laboratory module, while operating costs are estimated using Columbus’ share of total ISS habitable volume applied to current ISS operating expenses. All cost figures are adjusted to 2025 dollars using NASA’s New Start Inflation Index, which accounts for space technology-specific cost escalation.121212I exclude several cost categories from this analysis. Insurance costs, which can be significant for crewed systems, are omitted due to indications that private insurance markets lack capacity to cover fully privately owned crewed space stations (MacDonald et al., [2024](https://arxiv.org/html/2511.00935v1#bib.bib36)). Launch costs for initial system deployment are excluded, though including them would favor the shared core architecture. Training costs and supply-side structure details for crew operations are abstracted away, though transportation monopolies or inadequate training facilities could complicate the economics of human spaceflight. Integration costs for the core module are assumed to be 15% of total element costs—an assumption I make for analytical transparency. The resulting cost estimates provide a foundation for comparing the economic implications of different infrastructure sharing approaches.

Figure [2](https://arxiv.org/html/2511.00935v1#S3.F2 "Figure 2 ‣ 3 An application to commercial crewed space stations ‣ Public Infrastructure Investments for Space Market Development") shows an example of a core module, Figure [3](https://arxiv.org/html/2511.00935v1#S3.F3 "Figure 3 ‣ 3 An application to commercial crewed space stations ‣ Public Infrastructure Investments for Space Market Development") shows an example of a robotic arm, and Figure [4](https://arxiv.org/html/2511.00935v1#S3.F4 "Figure 4 ‣ 3 An application to commercial crewed space stations ‣ Public Infrastructure Investments for Space Market Development") shows an example of a habitat module.

![Refer to caption](images/GATEWAY__Moon_Space_Station_.png)


Figure 2: Artist’s concept of the Gateway’s PPE and HALO elements in lunar orbit. The PPE is the rectangular structure to which solar panels are attached, while the HALO is the cylindrical structure with circular docking ports visible. Credit: NASA.

![Refer to caption](images/Canadarm3--Canada_s-robotic-system-for-Gateway.jpg)


Figure 3: Artist’s concept of CSA’s Canadarm3, an exterior robotic arm, on the exterior of Gateway. Credit: CSA.

![Refer to caption](images/columbus-module-attached-to-harmony.png)


Figure 4: ESA’s Columbus laboratory module attached to the Harmony module on the ISS. Credit: ESA.

Table [2](https://arxiv.org/html/2511.00935v1#S3.T2 "Table 2 ‣ 3 An application to commercial crewed space stations ‣ Public Infrastructure Investments for Space Market Development") shows a list of core elements comprising a core module as described and, by analogy to roughly similar systems, approximate costs. Table [3](https://arxiv.org/html/2511.00935v1#S3.T3 "Table 3 ‣ 3 An application to commercial crewed space stations ‣ Public Infrastructure Investments for Space Market Development") shows the costs for a habitat module. All figures are expressed in millions of 2025 U.S. dollars and rounded to the nearest million.

Table 2: Core module element cost breakdown and annual costs

| Cost Component | Value | Source and Notes |
| --- | --- | --- |
| PPE and TTC | $453 M | Power distribution, thermal control, operational control for entire platform. Based on Gateway PPE contract NASA ([2020](https://arxiv.org/html/2511.00935v1#bib.bib42)). Adjusted from 2020 U.S. dollars. |
| Structure and outfitting | $1132 M | Node, module, shelter, docking, micrometeroid and orbital debris protection, internal pressurized volume outfitting. Based on Gateway HALO contract (NASA, [2021a](https://arxiv.org/html/2511.00935v1#bib.bib43)). Adjusted from 2021 U.S. dollars. |
| Robotic arm | $752 M | Station assembly, passive berthing, external operations. Based on Canadarm3 contract (CSA, [2024](https://arxiv.org/html/2511.00935v1#bib.bib13)). Adjusted from 2024 Canadian dollars. |
| Core module integration | $351 M | Assembling and integrating core structure elements. Assumption that integration costs are 15% the total cost of core elements. |
| Core module construction cost | $2688 M | Sum of rows above. |
| Construction cost annuity | $259 M/year | Annuitized over 15 years at 5%. |
| Operations cost | $250 M/year | Based on the operations costs for a private space station elicited from experts in Crane et al. ([2017](https://arxiv.org/html/2511.00935v1#bib.bib11)): “One industry expert estimated that operations costs for a modular space station could be $200 to $300 million.” |
| Core module total cost annuity | $509 M/year |  |




Table 3: Habitat module cost breakdown and annual costs

| Cost Component | Value | Source and Notes |
| --- | --- | --- |
| Construction cost | $1934 M | Based on the Columbus laboratory module, including testing and integration (DLR, [2023](https://arxiv.org/html/2511.00935v1#bib.bib17)). Adjusted from 2008 Euros. Columbus only has research racks without necessary support systems for crew bunks. |
| Construction cost annuity | $186 M/year | Annuitized over 15 years at 5%. |
| Operations cost | $267 M/year | Columbus has total volume of 75 m3 (ESA, [2025b](https://arxiv.org/html/2511.00935v1#bib.bib19)). ISS has total habitable volume of 388 m3 (NASA, [2025b](https://arxiv.org/html/2511.00935v1#bib.bib48)). 2021 NASA OIG found ISS operating expenses steady at roughly $1.2B/year over 2016-2020 (NASA, [2021b](https://arxiv.org/html/2511.00935v1#bib.bib44)). FY2026 NASA President’s Budget Request projects similar costs from 2025-2030 (NASA, [2025a](https://arxiv.org/html/2511.00935v1#bib.bib47)). Estimated as ISS total operating expenses scaled by Columbus’ share of habitable volume: (75/388)×1200(75/388)\times 1200. |
| Habitat module total cost annuity | $417 M/year |  |

These cost estimates allow direct application of the Section 2 framework to assess how the choice between independent stations and shared infrastructure affects competitive viability. Both architectures face identical expected economic conditions: $500M annually in market demand split between competitors, and $1B in total capturable program budget. The architectures differ in how this budget gets allocated between direct purchases from firms versus investment in shared infrastructure. In the independent free-flyer architecture, the program budget flows entirely to direct purchases ($500M per firm assuming two competitors). In the shared core architecture, the program invests in infrastructure—life support, power, docking, and robotic capabilities—that costs $509M annually based on the component estimates in Table [2](https://arxiv.org/html/2511.00935v1#S3.T2 "Table 2 ‣ 3 An application to commercial crewed space stations ‣ Public Infrastructure Investments for Space Market Development"), leaving $491M for direct purchases of habitat services ($246M per firm). I assume firms value the shared core functions identically whether provided by public infrastructure or developed independently.131313This reflects the functional equivalence of core capabilities across architectures. The shared core provides the same life support, power, and docking functions that firms would otherwise develop independently. The $509M annual value represents what firms would need to spend to develop equivalent capabilities, not necessarily the agency’s actual financing costs, which might differ due to existing assets, different financing terms, or economies of scale in procurement. Under this assumption, firms in the shared core architecture benefit from $509M in cost reduction while receiving $246M in direct agency purchases. Table [4](https://arxiv.org/html/2511.00935v1#S3.T4 "Table 4 ‣ 3 An application to commercial crewed space stations ‣ Public Infrastructure Investments for Space Market Development") presents the resulting economic parameters for both architectures, while Figure [5](https://arxiv.org/html/2511.00935v1#S3.F5 "Figure 5 ‣ 3 An application to commercial crewed space stations ‣ Public Infrastructure Investments for Space Market Development") maps these onto the sustainable competition diagram to show how well each approach can sustain competition.

Table 4: Economic parameters under alternative space station architectures

|  |  |  |
| --- | --- | --- |
|  | Independent free flyers | Shared core module |
|  | architecture | architecture |
| Desired number of competitors (NN) | 2 firms | 2 firms |
| Program budget (BB) | $1000 M/year | $1000 M/year |
| Direct investment (GiG\_{i}) | — | — |
| Direct purchases (RiGR^{G}\_{i}) | $500 M/year/firm | $246 M/year/firm |
| Shared infrastructure spending (GSG^{S}) | — | $509 M/year |
| Market revenue (RiMR^{M}\_{i}) | $250 M/year/firm | $250 M/year/firm |
| Shared infrastructure value (YGY^{G}) | — | $509 M/year |
| Gross total cost (XiX\_{i}) | $927 M/year/firm | $927 M/year/firm |
| Total industry revenues (RR) | $1500 M/year | $991 M/year |
| Total industry costs (CC) | $1855 M/year | $837 M/year |
| Total industry profits (Π\Pi) | -$355 M/year | $154 M/year |

Table [4](https://arxiv.org/html/2511.00935v1#S3.T4 "Table 4 ‣ 3 An application to commercial crewed space stations ‣ Public Infrastructure Investments for Space Market Development") shows that under the assumed conditions, the independent free-flyer architecture generates negative industry profits of $355M annually; two competing firms cannot both earn positive returns. Individual firms in this scenario face $927M in annual costs while receiving only $750M in combined government and market revenues ($500M from government purchases plus $250M from the market), resulting in $177M annual losses per firm. The shared core architecture, by contrast, generates positive industry profits of $154M annually, with each firm earning $77M in annual profits after accounting for the $509M cost reduction from shared infrastructure. Figure [5](https://arxiv.org/html/2511.00935v1#S3.F5 "Figure 5 ‣ 3 An application to commercial crewed space stations ‣ Public Infrastructure Investments for Space Market Development") maps these results onto the sustainable competition diagram. The free-flyer architecture falls into the region where only monopoly provision is economically viable, while the shared core architecture can sustain two firms. Under the shared core approach, firms earn profits available for reinvestment or dividends, though not enough to incent entry of additional competitors.

![Refer to caption](images/fig2-prod--diagram-example.png)


Figure 5: Sustainable competition diagram showing the relationship between industry-level direct government purchases, industry-level total costs, and the potential number of profitable firms for the crewed space stations example. Shaded regions indicate the expected sustainable number of competitors under different system cost and government-derived revenues.

### 3.1 Exploring alternative assumptions

The baseline analysis demonstrates how shared infrastructure can enable competition under a given set of conditions. The framework can also be used to explore how different assumptions affect economic architecture. Two economic variables deserve particular attention because they lie largely outside space agency planners’ control yet can significantly influence market development prospects: the scale of market demand for space station services, and the return expectations of private investors. Market demand reflects the broader commercial ecosystem for space-based research, manufacturing, and other applications—markets that may grow rapidly if early demonstrations prove successful, or remain limited if technical or economic barriers persist. Investor return expectations, meanwhile, fluctuate with broader macroeconomic conditions including interest rates, risk appetites, and alternative investment opportunities. By examining how the sustainable competition diagram changes under alternative values for these parameters, planners can assess the robustness of different economic architectures and identify conditions under which architectures might succeed.

Figure [6](https://arxiv.org/html/2511.00935v1#S3.F6 "Figure 6 ‣ 3.1 Exploring alternative assumptions ‣ 3 An application to commercial crewed space stations ‣ Public Infrastructure Investments for Space Market Development") shows how doubling market demand from $500M to $1B annually affects both architectures. This scenario reflects an optimistic case where early space station demonstrations catalyze broader commercial adoption across research institutions, pharmaceutical companies, manufacturing firms, and other potential users. Under these conditions, both architectures become more viable. The independent free-flyer architecture, which generated $355M in annual losses under baseline conditions, now produces positive industry profits and can sustain two competitors with margin for reinvestment or dividends. Each firm in the free-flyer scenario would earn $500M annually from non-government customers plus $500M from government purchases, covering the $927M total costs with $73M profit margin per firm. The shared core architecture performs even better, generating sufficient profits to sustain four competing firms rather than the two supported under baseline demand, with enough profits to provide returns to existing investors and potentially incent entry of additional competitors. Note, however, new entrants would not be able to enter on the same terms as incumbents without more capacity on the shared core or a new core. Further analysis of this scenario can identify threshold levels of market demand such that direct purchases alone may sustain competitive markets without requiring shared infrastructure. However, this outcome depends on successfully developing the commercial ecosystem—an uncertain prospect that may take years or decades to materialize, if ever.

![Refer to caption](images/fig2-prod--diagram-high-demand.png)


Figure 6: Sustainable competition diagram showing the relationship between industry-level direct government purchases, industry-level total costs, and the potential number of profitable firms for the crewed space stations example with market demand of $1000 M/year. Shaded regions indicate the expected sustainable number of competitors under different system cost and government-derived revenues.

Figure [7](https://arxiv.org/html/2511.00935v1#S3.F7 "Figure 7 ‣ 3.1 Exploring alternative assumptions ‣ 3 An application to commercial crewed space stations ‣ Public Infrastructure Investments for Space Market Development") shows how doubling investor return expectations from 5% to 10% annually affects both architectures. This scenario reflects tighter macroeconomic conditions where rising interest rates, increased risk premiums, or competition from alternative investments raise the hurdle rate for space technology projects. Under 10% return requirements, neither architecture can sustain two competing firms. The independent free-flyer architecture, already unprofitable for two firms under baseline conditions, becomes even less viable with higher costs of capital. The shared core architecture, which supported two firms under baseline conditions, also falls into the monopoly-only region. If there were two firms in the shared core architecture, both would require higher annual profits to compensate investors for the increased return requirement. But revenues and infrastructure-driven cost reductions remain unchanged, and expected cashflows that allowed firms to raise capital under baseline conditions no longer appear as attractive.

![Refer to caption](images/fig2-prod--diagram-high-rates.png)


Figure 7: Sustainable competition diagram showing the relationship between industry-level direct government purchases, industry-level total costs, and the potential number of profitable firms for the crewed space stations example with investor return expectations of 10%/year. Shaded regions indicate the expected sustainable number of competitors under different system cost and government-derived revenues.

These scenarios reveal several practical insights for public space agencies seeking to develop space markets. First, the choice between shared infrastructure and direct purchases can depend on economic conditions that are outside the agency’s control. Under favorable conditions—e.g., strong market demand and low capital costs—direct purchases may suffice to sustain competition without requiring shared infrastructure investments. Under challenging conditions—e.g., limited market demand or tight capital markets—even well-designed shared infrastructure may prove insufficient to maintain competitive supply. Second, given how external economic factors can dominate program design choices in determining market outcomes, timing market development efforts to coincide with favorable economic conditions may be as important as program design choices. Third, the framework provides a systematic way to assess these trade-offs and communicate them to stakeholders, but depends on credible estimates of costs, market demand, and competitive dynamics that remain challenging to develop for novel space technology systems. The estimates may evolve with technical and economic conditions, requiring ongoing assessment and planning.

## 4 Future Research Directions

I have demonstrated the use of a simple framework to map the number of firms that can profitably provide goods and services derived from a space technology system under different public funding and industry cost structures. The framework demonstrates the multiplier effect of non-rival benefits from shared infrastructure and the sensitivity of market development programs to non-technological factors like market demand expectations and investor return requirements. Though highly stylized, the framework’s simplicity may support its use as an analytical and communications tool under real-world conditions. However, effective use requires considerable expertise with space technology systems to construct relevant element costs, identify opportunities for efficient shared infrastructure, and assess whether candidate system architectures will meet public objectives. This expertise is generally not economists’ comparative advantage, but is often present within public space agencies. Productive use of this framework therefore requires an iterative process between economists, engineers, and planners at public space agencies, with extensive engagement with industry to obtain parameter estimates and institutional detail.

This framework may be most useful as a way to formalize, consolidate, and communicate the various technical and economic assumptions that planners in public space agencies and in industry have adopted. The exercises I have conducted here hopefully help economists see the kinds of insights public space agency planners may be able to use, while also helping public space agency planners see fundamental economic issues more clearly. Making such frameworks practical requires better capabilities in several areas.

### 4.1 Measuring the Space Economy

Accurate measurement of space economy size and growth is essential for rational planning and investment decisions. Industry associations and investment banks project dramatic growth, with some forecasting markets reaching $1.8 trillion by 2035 (Daswani et al., [2022](https://arxiv.org/html/2511.00935v1#bib.bib15); Khlystov et al., [2024](https://arxiv.org/html/2511.00935v1#bib.bib29)). Independent analyses reveal these kinds of estimates often systematically overstate growth, e.g., by double-counting government revenues and input costs (Crane et al., [2020](https://arxiv.org/html/2511.00935v1#bib.bib12)). Despite these measurement problems, academic research often relies on industry projections that assume input costs have fallen dramatically and will continue declining and output markets are competitive, implicitly or explicitly assuming competition in space-related goods and services will continue increasing (Rao et al., [2020](https://arxiv.org/html/2511.00935v1#bib.bib54); Adilov et al., [2022](https://arxiv.org/html/2511.00935v1#bib.bib2); Nozawa et al., [2023](https://arxiv.org/html/2511.00935v1#bib.bib50); Stuermer et al., [2023](https://arxiv.org/html/2511.00935v1#bib.bib58); Metzger, [2023](https://arxiv.org/html/2511.00935v1#bib.bib38); Bongers et al., [2025](https://arxiv.org/html/2511.00935v1#bib.bib4)).

These assumptions contradict both economic theory and emerging empirical evidence about space markets. High fixed costs, limited market demand, non-market motivations, and substitutability with terrestrial alternatives constrain entry and long-run competition (Triezenberg et al., [2020](https://arxiv.org/html/2511.00935v1#bib.bib60); Guyot et al., [2023](https://arxiv.org/html/2511.00935v1#bib.bib25)). Supply constraints persist despite market development efforts (Triezenberg et al., [2024](https://arxiv.org/html/2511.00935v1#bib.bib61); Rao and Colvin, [2025](https://arxiv.org/html/2511.00935v1#bib.bib52)), launch prices for some government customers have increased in real terms (Kim, [2025](https://arxiv.org/html/2511.00935v1#bib.bib31)), and U.S. space manufacturing capacity utilization has remained flat at about 63% since 2016 (Highfill and Rao, [2025](https://arxiv.org/html/2511.00935v1#bib.bib27)). While real growth in U.S. space manufacturing has exceeded overall U.S. space economy growth (Highfill and Weinzierl, [2024](https://arxiv.org/html/2511.00935v1#bib.bib28)), the persistence of supply constraints suggests structural economic factors may matter more than space-specific policy choices. Better measurement of the space economy can help planners develop better assessments of current conditions, evaluate past market development efforts, and assess the plausibility of projected growth scenarios.

### 4.2 Estimating Demand for Advanced Technology Systems

In sectors like space launch, statistical estimates of demand can be constructed from historical data (Triezenberg et al., [2020](https://arxiv.org/html/2511.00935v1#bib.bib60); MITRE, [2021](https://arxiv.org/html/2511.00935v1#bib.bib39); Adilov et al., [2022](https://arxiv.org/html/2511.00935v1#bib.bib2)). This is less feasible for markets like lunar sample return or lunar surface power, where necessary capabilities do not currently exist. Yet as the framework developed here shows, market demand estimates are critical to designing successful economic architectures.

Developing principled estimates of the scale and elasticity of demand over longer timescales (e.g., 15+ years) for markets that don’t yet exist and have few close analogs—like lunar surface power—is challenging. A structural economic model may be able to measure this demand, e.g., by varying engineering parameters to estimate the total benefit derived from the good or service as in Colvin et al. ([2020b](https://arxiv.org/html/2511.00935v1#bib.bib10)) and Metzger ([2023](https://arxiv.org/html/2511.00935v1#bib.bib38)), though the relevant preference and technology primitives often require technical knowledge that economists don’t possess. While advances in theory may enable better modeling of such markets, survey and qualitative research methods targeted at relevant stakeholders may provide sufficient institutional detail to usefully constrain models and parameter values. Developing transparent and principled demand and willingness-to-pay estimates for such systems, and communicating them effectively to public space agency planners, may significantly improve the quality of economic architectures for space technology systems.

### 4.3 Estimating Cost Differentials Across Economic Architectures

Effective use of this framework requires accurate assessment of cost differentials across economic architectures. I assumed both economic architectures had identical costs; this is unlikely in practice. In particular, there is a widespread perception in the space sector that firm fixed-price (FFP) contracts or private development result in lower costs than cost-plus fixed fee (CPFF) contracts or government oversight. These beliefs underlie advocacy for FFP contracting (Vozoff, [2009](https://arxiv.org/html/2511.00935v1#bib.bib63); Murray, [2023](https://arxiv.org/html/2511.00935v1#bib.bib40); Berger, [2023](https://arxiv.org/html/2511.00935v1#bib.bib3)) and assumptions that industry-led projects will cost less than government-led projects.141414For example, Crane et al. ([2017](https://arxiv.org/html/2511.00935v1#bib.bib11)) assumed industry-led projects cost 30% less than equivalent government-led projects in estimating the profitability of private space stations. This assumption was conservative in the context of the analysis it served, but not a neutral one for economic architecture assessments: it would tend to make direct purchases and transfers systematically appear more cost-effective than shared infrastructure investments.

Empirical evidence challenges these beliefs. Kim ([2025](https://arxiv.org/html/2511.00935v1#bib.bib31)) found NASA has paid increasing real costs for launch services despite using FFP contracts with providers competing in markets where NASA is one among many customers. Carril and Duggan ([2020](https://arxiv.org/html/2511.00935v1#bib.bib6)) found the U.S. Department of Defense’s transition from FFP to CPFF contracts during a period of industry consolidation did not statistically significantly increase costs. Kim and Hyde ([2025](https://arxiv.org/html/2511.00935v1#bib.bib32)) found industry-led projects show statistically significant cost advantages over government-led projects only for low-risk systems like small satellites. Indeed, simple logic suggests FFP contracts may create “loser’s curse” effects: if contractors can exit when costs exceed expectations, FFP mechanisms transfer upside to contractors while leaving agencies exposed to downside risk.151515This is not just a theoretical concern. In 2022, NASA awarded Collins Aerospace a FFP contract under the xEVAS program to develop and produce space suits for ISS missions. The contract would have involved NASA leasing rather than purchasing the suits from Collins, with Collins retaining ownership and the ability to offer the suits to other customers, such as crew on future private space stations (Foust, [2022](https://arxiv.org/html/2511.00935v1#bib.bib22)). In 2024, Collins withdrew from the contract (Foust, [2024](https://arxiv.org/html/2511.00935v1#bib.bib23)). Industry sources suggested that the company faced a combination of cost and schedule overruns and had determined that continued work on the contract was unprofitable. It is unclear what kind of market demand forecasts were used by NASA and Collins when developing the economic architecture for the xEVAS program, and how Collins’ view of the space suits market evolved afterwards. Some observers have speculated that Boeing’s Starliner project may face a similar fate if Boeing decides the LEO crew transportation market is not worth the marginal development effort required (Terlep and Maidenberg, [2025](https://arxiv.org/html/2511.00935v1#bib.bib59)). Given how thoroughly the space community has internalized beliefs about contract type and governance effects on costs, credible econometric analysis could significantly improve acquisition strategies.

### 4.4 The Relative Value of Government and Market Demand to Private Investors

I have assumed that all revenues, whether derived from government direct transfers, government direct purchases, or market demand, are viewed identically by investors in space technology systems. Is this a reasonable assumption? How do investor perceptions of space-derived cashflows vary with market and government budget volatility? Analyses like event studies of public space company stock prices around contract announcements, surveys of private space investors about their investment evaluation criteria, and choice experiments to elicit investor preferences about uncertain revenue streams could provide quantitative estimates of any systematic differences in how investors in space technology system perceive different revenue sources.

### 4.5 Analyzing Economic Architectures for Other Space Applications

I have illustrated how principles of economic architecture can help shape programs to develop markets for crewed space services. Triezenberg et al. ([2020](https://arxiv.org/html/2511.00935v1#bib.bib60), [2024](https://arxiv.org/html/2511.00935v1#bib.bib61)) provide detailed analyses of similar goals and trade-offs in the U.S. National Security Space launch market, showing how acquisition decisions affect the number of sustainable competitors. Economic architecture principles can also be applied to orbital debris risk reduction—one of the most studied aspects of space economics in recent years. While grab-and-remove active debris removal (ADR) systems can be cost-ineffective at reducing risk (Colvin et al., [2023](https://arxiv.org/html/2511.00935v1#bib.bib8); Locke et al., [2024](https://arxiv.org/html/2511.00935v1#bib.bib34)), governments may want to support grab-and-remove technologies for non-economic reasons—such capabilities involve intermediate technologies with military applications, like grappling and relocating non-cooperative objects.

Ultimately, space sustainability programs may require combinations of technologies best provided by different types of actors. Rao et al. ([2025](https://arxiv.org/html/2511.00935v1#bib.bib53)) assessed the economic efficiency of portfolios of space sustainability investments including actions and technologies to mitigate risk (e.g., additional shielding against small debris), to remediate risk (e.g., grabbing and removing large debris), and to improve tracking capabilities (e.g., additional radar systems). They identified a class of efficient portfolios containing grab-and-remove ADR that also contain ground-based lasers to remove small debris, new ground-based tracking systems, and improved shielding. Public ownership may be necessary for ground-based laser systems that remove small debris and nudge large objects away from collision trajectories, both due to non-economic factors and because these systems provide non-rival benefits to all satellite operators. Similar considerations may also apply to some ground-based tracking systems that provide baseline situational awareness of the space environment. Direct investments and purchases could seed and support private firms developing and offering ADR services or shielding to satellite operators. The economic architecture questions mirror those in the space station case: determining budget allocation, assessing market demand for debris removal services and shielding, evaluating the distribution of collision risks across satellite operators, and accounting for non-economic factors that influence technology deployment decisions.

## 5 Conclusion

This essay addresses a fundamental challenge facing public space agencies: how to allocate limited budgets between direct purchases, direct transfers, and shared infrastructure investments to develop and sustain markets for advanced technology systems. The core economic insight—that shared infrastructure creates non-rival benefits that can sustain more competitors per marginal dollar than direct support mechanisms—follows from standard principles of public economics (Samuelson, [1954](https://arxiv.org/html/2511.00935v1#bib.bib55)). The commercial space station application demonstrates this: under plausible conditions, public investment in shared core infrastructure enables two competing firms to earn substantial profits, while allocating that budget entirely toward direct purchases alone results in industry-wide losses. The sustainable competition diagram makes these kinds of effects transparent to decision-makers.

This framework applies broadly to advanced technology domains with high fixed costs, uncertain market demand, non-market motivations, and separable system functions enabling shared infrastructure. Public science and technology agencies in such sectors face similar tensions between procurement objectives and market development goals, while private investors must evaluate opportunities where government decisions can matter more than market fundamentals. Recent experience provides sobering evidence of these constraints: Collins Aerospace’s withdrawal from NASA’s xEVAS contract shows how market forces can overwhelm program design choices.

As global investment in advanced technologies accelerates, frameworks that help planners systematically compare economic architectures will become more valuable to organizations seeking to develop markets for these systems. However, significant shares of demand for these systems are often driven by non-economic motivations. Analyses focused on first-best regulatory pathways to maximize economic welfare rather than second-best investment strategies to support particular goals can miss opportunities for policy relevance. Market development plans require theoretical and empirical foundations that make economic analysis credible and actionable for the organizations that must implement them.

## Declarations

No funding was received for conducting this study.

## References

* (1)
* Adilov et al. (2022)

  Adilov, Nodir, Peter Alexander, Brendan Cunningham, and Nikolas Albertson, “An analysis of launch cost reductions for low Earth orbit satellites,” Economics Bulletin, September 2022, 42 (3).
* Berger (2023)

  Berger, Eric, “Weirdly, a NASA official says fixed-price contracts do the agency “no good”,” June 2023.
* Bongers et al. (2025)

  Bongers, Anelí, César Ortiz, and José L. Torres, “DISE: A Dynamic Integrated Space-Economy Model for Orbital Debris Mitigation Policy Evaluation,” Environmental and Resource Economics, August 2025, 88 (8), 2125–2156.
* Cabinet Office, Government of Japan (2024)

  Cabinet Office, Government of Japan, “Space Strategy Fund: Space Policy,” 2024.
* Carril and Duggan (2020)

  Carril, Rodrigo and Mark Duggan, “The impact of industry consolidation on government procurement: Evidence from Department of Defense contracting,” Journal of Public Economics, April 2020, 184, 104141.
* Castro-Wallace et al. (2017)

  Castro-Wallace, Sarah L., Charles Y. Chiu, Kristen K. John, Sarah E. Stahl, Kathleen H. Rubins, Alexa B. R. McIntyre, Jason P. Dworkin, Mark L. Lupisella, David J. Smith, Douglas J. Botkin, Timothy A. Stephenson, Sissel Juul, Daniel J. Turner, Fernando Izquierdo, Scot Federman, Doug Stryke, Sneha Somasekar, Noah Alexander, Guixia Yu, Christopher E. Mason, and Aaron S. Burton, “Nanopore DNA Sequencing and Genome Assembly on the International Space Station,” Scientific Reports, December 2017, 7 (1), 18022.
  Publisher: Nature Publishing Group.
* Colvin et al. (2023)

  Colvin, Thomas J, John Karcz, and Grace Wusk, “Cost and Benefit Analysis of Orbital Debris Remediation,” Technical Report, NASA Office of Technology, Policy, and Strategy March 2023.
* Colvin et al. (2020a)

  Colvin, Thomas J., Keith Crane, and Bhavya Lal, “Assessing the economics of asteroid-derived water for propellant,” Acta Astronautica, November 2020, 176, 298–305.
* Colvin et al. (2020b)

  Colvin, Thomas J, Keith W Crane, and Rachel Lindbergh, “Demand Drivers of the Lunar and Cislunar Economy,” Technical Report D-13219, Science and Technology Policy Institute April 2020.
* Crane et al. (2017)

  Crane, Keith W, Benjamin A Corbin, Bhavya Lal, Reina S Buenconsejo, Danielle Piskorz, and Annalisa L Weigel, “Market Analysis of a Privately Owned and Operated Space Station,” Technical Report P-8247, Science and Technology Policy Institute March 2017.
* Crane et al. (2020)

    , Bhavya Lal, and Rachel Y Wei, “Measuring the Space Economy: Estimating the Value of Economic Activities in and for Space,” Technical Report D-10814, Science and Technology Policy Institute March 2020.
* CSA (2024)

  CSA, “Canada begins detailed design, construction and testing of Canadarm3 for Gateway,” June 2024.
  Last Modified: 2024-06-27.
* Danau and Vinella (2015)

  Danau, Daniel and Annalisa Vinella, “Public-Private Contracting under Limited Commitment,” Journal of Public Economic Theory, 2015, 17 (1), 78–110.
  \_eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1111/jpet.12113.
* Daswani et al. (2022)

  Daswani, Pavan, Anita McBain, Amit B Harchandani, Anthony Nemoto, Jenny Ping, Michael Rollins, Amir Blachman, Nanne Tolsma, Charles J Armitage, Samuel Burgess, Tahmid Islam, Nithin Pejaver, Ephrem Ravi, Sathish B Sivakumar, Simon Drake, and Scott Wisniewski, “Space: The Dawn of a New Age,” Technical Report, Citi GPS May 2022.
* Selding (2014)

  de Selding, Peter B., “ESA Says It Is on Track To Reduce Its Station Costs by 30 Percent,” January 2014.
* DLR (2023)

  DLR, “The Eu­ro­pean Colum­bus Lab­o­ra­to­ry,” May 2023.
  Deutsches Zentrum fur Luft- und Raumfahrt.
* ESA (2025a)

  ESA, “ESA Strategy 2040,” 2025.
* ESA (2025b)

    , “European Columbus laboratory,” 2025.
* European Commission (2025)

  European Commission, “EU Space Act,” 2025.
* EY Global (2024)

  EY Global, “Japan launches substantial 10-year fund to accelerate space business development R&D,” June 2024.
* Foust (2022)

  Foust, Jeff, “Collins Aerospace selected to develop new space station spacesuit,” December 2022.
* Foust (2024)

    , “Collins Aerospace pulls back from NASA spacesuit contract,” June 2024.
* Foust (2025)

    , “NASA extends seat barter agreement with Roscosmos into 2027,” April 2025.
* Guyot et al. (2023)

  Guyot, Julien, Akhil Rao, and Sébastien Rouillon, “Oligopoly competition between satellite constellations will reduce economic welfare from orbit use,” Proceedings of the National Academy of Sciences, October 2023, 120 (43), e2221343120.
  Publisher: Proceedings of the National Academy of Sciences.
* Henderson et al. (2012)

  Henderson, J. Vernon, Adam Storeygard, and David N. Weil, “Measuring Economic Growth from Outer Space,” American Economic Review, April 2012, 102 (2), 994–1028.
* Highfill and Rao (2025)

  Highfill, Tina and Akhil Rao, “Measuring Space Manufacturing Plant Utilization and Own-Account Production,” Technical Report WP2025-5, U.S. Bureau of Economic Analysis April 2025.
* Highfill and Weinzierl (2024)

     and Matthew Weinzierl, “Real growth in space manufacturing output substantially exceeds growth in the overall space economy,” Acta Astronautica, June 2024, 219, 236–242.
* Khlystov et al. (2024)

  Khlystov, Nikolai, Alizée Acket-Goemaere, Richard F. Ambrose, Ryan Brukardt, Jesse Klempner, Andrew Sierra, and Brooke Stokes, “Space: the $1.8T Opportunity for Global Economic Growth,” Technical Report, World Economic Forum; McKinsey & Company April 2024.
* Kim (2023)

  Kim, Moon J., “Toward Coherence: A Space Sector Public-Private Partnership Typology,” Space Policy, May 2023, 64, 101549.
* Kim (2025)

    , “Counting stars and costs: An empirical examination of space launch cost trend at NASA,” Acta Astronautica, July 2025, 232, 633–639.
* Kim and Hyde (2025)

     and Tupper Hyde, “In and Out: Comparative Analysis of NASA and Industry Spacecraft Costs,” Journal of Spacecraft and Rockets, 2025, Forthcoming.
* Laffont and Tirole (1993)

  Laffont, Jean-Jacques and Jean Tirole, A Theory of Incentives in Procurement and Regulation, Cambridge, MA, USA: MIT Press, March 1993.
* Locke et al. (2024)

  Locke, Jericho, Thomas J. Colvin, Laura Ratliff, Asaad Abdul-Hamid, and Colin Samples, “Cost and Benefit Analysis of Mitigating, Tracking, and Remediating Orbital Debris,” Technical Report May 2024.
  NTRS Author Affiliations: National Aeronautics and Space Administration, Stevens Institute of Technology, Logistics Management Institute (United States) NTRS Document ID: 20240003484 NTRS Research Center: Headquarters (HQ).
* MacDonald (2017)

  MacDonald, Alexander, The Long Space Age: The Economic Origins of Space Exploration from Colonial America to the Cold War, Yale University Press, 2017.
* MacDonald et al. (2024)

    , Dan Thomas, and Ben Roberts, “Commercial LEO Destinations Asset and Liability Insurance: Findings and Options,” Technical Report, NASA Office of Technology, Policy, and Strategy September 2024.
* Magalhães et al. (2021)

  Magalhães, Tiago E. C., Diogo E. C. G. Silva, Carlos E. C. G. Silva, Afonso A. Dinis, José P. M. Magalhães, and Tânia M. Ribeiro, “Observation of atmospheric gravity waves using a Raspberry Pi camera module on board the International Space Station,” Acta Astronautica, May 2021, 182, 416–423.
* Metzger (2023)

  Metzger, Philip T., “Economics of in-space industry and competitiveness of lunar-derived rocket propellant,” Acta Astronautica, June 2023, 207, 425–444.
* MITRE (2021)

  MITRE, “The Global Commercial Market for Small Satellite Orbital Launch Services: Determinants of Customers’ Choice of Launch Provider,” Technical Report, Department of the Air Force Office of Commercial and Economic Analysis November 2021.
* Murray (2023)

  Murray, Robert, “The NewSpace market: Capital, control, and commercialization,” Technical Report, Atlantic Council Scowcroft Center for Strategy and Security April 2023.
* NASA (2019)

  NASA, “NASA Plan for Commercial LEO Development,” Technical Report, NASA May 2019.
* NASA (2020)

    , “NASA Awards Artemis Contract for Lunar Gateway Power, Propulsion - NASA,” March 2020.
* NASA (2021a)

    , “NASA, Northrop Grumman Finalize Moon Outpost Living Quarters Contract - NASA,” 2021.
  Section: Commercial Space.
* NASA (2021b)

    , “NASA’s Management of the International Space Station and Efforts to Commercialize Low Earth Orbit,” Technical Report IG-22-005, NASA Office of Inspector General November 2021.
* NASA (2022)

    , “Benefits for Exploration: International Space Station Factsheet,” Technical Report 2022.
* NASA (2024)

    , “NASA’s Low Earth Orbit Microgravity Strategy,” Technical Report December 2024.
* NASA (2025a)

    , “FY 2026 Budget Technical Supplement,” Technical Report, NASA 2025.
* NASA (2025b)

    , “International Space Station Facts and Figures,” 2025.
  Section: Humans in Space.
* NASA Executive Cost Analysis Steering Group (2015)

  NASA Executive Cost Analysis Steering Group, NASA Cost Estimating Handbook, 4.0 ed., NASA, February 2015.
* Nozawa et al. (2023)

  Nozawa, Wataru, Kenichi Kurita, Tetsuya Tamaki, and Shunsuke Managi, “To What Extent Will Space Debris Impact the Economy?,” Space Policy, November 2023, 66, 101580.
* Proctor et al. (2021)

  Proctor, Nicholas, Ensieh Shojaeddini, Angel Abbud-Madrid, Peter Maniloff, and Ian Lange, “Feasibility of space solar power for remote mining operations,” Acta Astronautica, September 2021, 186, 183–189.
* Rao and Colvin (2025)

  Rao, Akhil and Thomas J. Colvin, “Opportunity Costs Drive the Market Price of Starship Launches,” Technical Report, Rational Futures May 2025.
* Rao et al. (2025)

    , Jericho Locke, and Thomas J. Colvin, “Cost-Benefit Analysis of Debris Risk Reduction Portfolios,” Technical Report June 2025.
  NTRS Author Affiliations: NASA Intergovernmental Personnel Act (IPA) Employee, National Aeronautics and Space Administration NTRS Document ID: 20250005977 NTRS Research Center: Headquarters (HQ).
* Rao et al. (2020)

    , Matthew G. Burgess, and Daniel Kaffine, “Orbital-use fees could more than quadruple the value of the space industry,” Proceedings of the National Academy of Sciences, June 2020, 117 (23), 12756–12762.
  Publisher: Proceedings of the National Academy of Sciences.
* Samuelson (1954)

  Samuelson, Paul A., “The Pure Theory of Public Expenditure,” The Review of Economics and Statistics, November 1954, 36 (4), 387–389.
* Smith (2025)

  Smith, Marcia, “RIFs at NASA Headquarters Begin,” March 2025.
* SpaceRef (2019)

  SpaceRef, “Alexander MacDonald Named NASA’s Chief Economist,” September 2019.
* Stuermer et al. (2023)

  Stuermer, Martin, Maxwell Fleming, Ian Lange, and Sayeh Shojaeinia, “Growth and Resources in Space: Pushing the Final Frontier?,” Proceedings of the National Academy of Sciences, 2023, TBD (TBD), TBD.
  Publisher: National Acad Sciences.
* Terlep and Maidenberg (2025)

  Terlep, Sharon and Micah Maidenberg, “Boeing explores sale of space business,” The Wall Street Journal, October 2025.
* Triezenberg et al. (2020)

  Triezenberg, Bonnie L., Colby P. Steiner, Grant Johnson, Jonathan Cham, Éder M. Sousa, Moon Kim, and Mary Kate Adgie, “Assessing the Impact of U.S. Air Force National Security Space Launch Acquisition Decisions: An Independent Analysis of the Global Heavy Lift Launch Market,” Technical Report April 2020.
* Triezenberg et al. (2024)

    , Éder M. Sousa, Emily Allendorf, Hansell Perez, Jonathan Roberts, and Mack Rodgers, “Assessing the Impact of U.S. Air Force National Security Space Launch Acquisition Decisions: 2023 Update,” Technical Report September 2024.
* Veldhuyzen and Grifoni (1999)

  Veldhuyzen, R and E Grifoni, “No Exchange of Funds – The ESA Barter Agreements for the International Space Station,” ESA Bulletin, 1999, 99.
* Vozoff (2009)

  Vozoff, Max, “”COTS-like”: the future of space procurement,” 2009.
* Weinzierl (2018)

  Weinzierl, Matthew, “Space, the Final Economic Frontier,” Journal of Economic Perspectives, May 2018, 32 (2), 173–192.
  Publisher: American Economic Association.
* Werner (2024)

  Werner, Debra, “Flawless Photonics Kicking Glass,” February 2024.