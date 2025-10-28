---
authors:
- Ruaridh Macdonald
- Filippo Pecci
- Luca Bonaldo
- Jun Wen Law
- Yu Weng
- Dharik Mallapragada
- Jesse Jenkins
doc_id: arxiv:2510.21943v1
family_id: arxiv:2510.21943
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'MacroEnergy.jl: A large-scale multi-sector energy system framework'
url_abs: http://arxiv.org/abs/2510.21943v1
url_html: https://arxiv.org/html/2510.21943v1
venue: arXiv q-fin
version: 1
year: 2025
---


Ruaridh Macdonald 


Filippo Pecci 
RFF-CMCC European Institute on Economics and the Environment,
Italy

Luca Bonaldo 
Princeton University, USA

Jun Wen Law 
Massachusetts Institute of Technology, USA

Yu Weng 
Massachusetts Institute of Technology, USA

Dharik Mallapragada 
New York University, USA

Jesse Jenkins 
Princeton University, USA

(24 October 2025)

## Summary

MacroEnergy.jl (aka Macro) is an open-source framework for multi-sector
capacity expansion modeling and analysis of macro-energy
systems([]). It is written
in Julia ([]) and
uses the JuMP ([])
package to interface with a wide range of mathematical solvers. It
enables researchers and practitioners to design and analyze energy and
industrial systems that span electricity, fuels, bioenergy, steel,
chemicals, and other sectors. The framework is organized around a small
set of sector-agnostic components that can be combined into flexible
graph structures, making it straightforward to extend to new
technologies, policies, and commodities. Its companion packages support
decomposition methods and other advanced techniques, allowing users to
scale models across fine temporal and spatial resolutions.
MacroEnergy.jl provides a versatile platform for studying energy
transitions at the detail and scale demanded by modern research and
policy.

## Statement of Need

The increasing complexity of energy systems necessitates advanced
modeling tools to support decision-making in infrastructure planning,
R&D decisions and policy design. This complexity comes from the
challenge of ensuring the reliability of grids with large amounts of
renewable generation and storage, increased coupling and electrification
of energy-intensive sectors, greater diversity in the technologies and
policies being deployed, and many other factors.

Capacity expansion modelling frameworks have improved substantially in
recent years. A wider range of problems can now be solved thanks to
improvements in the underlying formulations and solvers while access to
richer data sources has enabled more realistic representations of
resources, weather and demand. Looking ahead, further improvements are
on the horizon, including non-linear technology formulations that
capture richer trade-offs ([]; [];
[]), tighter integration
with integrated assessment models and other tools
([];
[];
[]), and novel
approaches to scaling up problem size
([];
[];
[]).

There has also been some convergence in the design and capabilities of
modelling frameworks as the field comes to understand what is required
to produce robust, policy-relevant results. Recent studies suggest that
capacity expansion models must consider decades of operational data
([];
[]), may require
temporal resolution as fine as five minutes
([];
[]), and
should capture spatial heterogeneity at the county level
([];
[];
[];
[]). In addition,
they must be able to represent a wide variety of coupled sectors as the
majority of emission reductions will come from outside the electricity
sector. Electricity-centric frameworks; such as PyPSA
([]), GenX
([]),
Calliope ([]), and others ([];
[];
[];
[]); developed the
computational capabilities needed to optimize grids over long time
series of hourly or sub-hourly data in order to properly incorporate
variable renewable energy generation and storage. In recent years,
several have begun to extending their frameworks to include other
sectors, such as hydrogen, fuels, and industrial processes. On the other
hand, economy-wide models; such as TIMES
([]), TEMOA
([]) and others;
have long been able to represent multiple sectors though the use of
flexible graph-based structures. However, they do not have the
computational performance required to include long, high-resolution time
series.

Extending existing models to new sectors or to dramatically improve
performance often requires rewriting core routines or layering new
modules on top. This complicates validation, obscures interactions
across the system, and leaves the codebase hard to maintain. In the
authors’ experience from previous development, the frameworks remain
architectured around their original sectors, making it problematic to
exclude those sectors and quickly increasing the difficulty and time
required to add new features.

MacroEnergy.jl was designed to overcome these limitations. Its
architecture is based on a small set of sector-agnostic components that
can be combined into graphs to represent networks, technologies, and
policies in any sector. Features are largely independent of one another,
allowing users to focus on how best to represent their technology or
policy of interest instead of working around the existing code.

MacroEnergy.jl is also designed from the ground-up to scale to large,
multi-sector problems. Modeling across coupled sectors greatly increases
runtimes, often making problems intractable
([]). Techniques
such as model compression and the use of representative periods can ease
the computational burden, but eventually large-scale models reach the
limits of what can be solved on a single computing node. To scale
further, methods which allow models to be solved across computing
clusters are essential. MacroEnergy.jl was designed with these
challenges in mind. Its data structures and graph-based representation
of energy systems enable sectoral, temporal and spatial decompositions
by default. It also includes a suite of companion packages, which
provide advanced decomposition algorithms
([]),
automatic model scaling
([]), and
example systems
([]). Other companion packages are under development. These will
provide representative period selection and other tools to enhance
MacroEnergy.jl. MacroEnergy.jl and its companion packages are registered
Julia packages and are freely available on GitHub or through the Julia
package manager.

## Use Cases

MacroEnergy.jl can be used to optimize the design and operation of
energy and industrial systems, investigate the value of new technologies
or polices, optimize investments in an energy system over multiple
years, and many other tasks. It is being used for several ongoing
investigations of regional energy systems, including as part of the
Net-Zero X Global Initiative - a research consortium involving top
research institutions around the world developing shared modeling
methods and completing detailed, actionable country-specific studies
supporting net-zero transitions.

The framework was designed with three user profiles in mind. Where
possible, we have passed modelling complexity upstream to developers, so
that most users can build and run models faster and with less coding
knowledge.

* •

  Users: Want to create and optimize a real-world system using
  MacroEnergy.jl. They should be able to do this with little or no
  coding, and without knowledge of MacroEnergy.jl’s components or
  internal structure.
* •

  Modelers: Want to add new assets, sectors, or public policies to
  MacroEnergy.jl. They will need to be able to code in Julia and
  understand some of MacroEnergy.jl’s components, but they do not
  require knowledge of its internal structure or underlying packages.
* •

  Developers: Want to change or add new features, model formulations or
  constraints to MacroEnergy.jl. They will require detailed knowledge of
  MacroEnergy.jl’s components, internal structure, and underlying
  packages.

## Structure

MacroEnergy.jl models are made up of four core components which are used
to describe the production, transport, storage and consumption of
various commodities. The components can be connected into multi-sectoral
networks of commodities. They are commodity-agnostic so can be used for
any flow of a good, energy, etc. While we believe MacroEnergy.jl will
most often be used to study energy systems, commodities can also be
data, money, or more abstract flows.

The four core components are:

1. 1.

   Edges: describe and constrain the flow of a commodity
2. 2.

   Nodes: balance flows of one commodity and allow for exogenous flows
   into and out of a model. These can be used to represent exogenous
   demand or supply of a commodity.
3. 3.

   Storage: allow for a commodity to be stored over time.
4. 4.

   Transformations: allow for the conversion of one commodity into
   another by balancing flows of one or more commodities.

These four core components can be used directly to build models but most
users will find it easier to combine them into Assets and Locations.
Assets are collections of components that represent real-world
infrastructure such as power plants, industrial facilities, transmission
lines, etc. For example, a water electrolyzer asset would include edges
for electricity and water inputs and hydrogen output, and a
transformation to conver between them. Locations are collections of
Nodes which represent physical places where assets are situated and
commodities can be transported between. While Edges can only connect to
Nodes of the same Commodity, Locations are an abstraction that
simplifies the user-input required to connect different commodities
across physical places. Together, Assets and Locations allow for models
to be truer to life and easier to analyze.

Assets and Locations in turn form Systems which represent an energy
and/or industrial system. Most often, each System will be optimized
separately given a user-defined operating period. Several Systems can be
combined into a Case. Cases can be used for multi-stage capacity
expansion models, rolling-horizon optimization, sensitivity studies, and
other work requiring multiple snapshots or versions of an energy system.
MacroEnergy.jl can automatically manage the running of these different
Cases for users, either directly or in combination with
MacroEnergySolver.jl package.

## Acknowledgements

The development of MacroEnergy.jl was funded by the Schmidt Sciences
Foundation. This publication was based (fully or partially) upon work
supported by the U.S. Department of Energy’s Office of Energy Efficiency
and Renewable Energy (EERE) under the Hydrogen Fuel Cell Technology
Office, Award Number DE-EE0010724. The views expressed herein do not
necessarily represent the views of the U.S. Department of Energy or the
United States Government.

## References

## References

* Bezanson, J., Edelman, A., Karpinski, S., & Shah, V. B. (2017). Julia:
  A fresh approach to numerical computing. *SIAM Review*,
  *59*(1), 65–98.
* Blair, N., Dobos, A. P., Freeman, J., Neises, T., Wagner, M., Ferguson,
  T., Gilman, P., & Janzou, S. (2014). *System advisor model, sam
  2014.1. 14: General description*. National Renewable Energy Lab.(NREL),
  Golden, CO (United States).
* Brown, P., Carag, V., Chen, Y., Chernyakhovskiy, I., Cohen, S., Cole,
  W., Duraes de Faria, V., Gagnon, P., Halloran, C., Hamilton, A., Ho, J.,
  Mindermann, K., Mowers, J., Mowers, M., Obika, K., Pham, A., Schleifer,
  A., Sergi, B., Serpe, L., … Vanatta, M. (n.d.). *Regional
  Energy Deployment System Model 2.0 (ReEDS 2.0)*.
  <https://www.nrel.gov/analysis/reeds/index.html>
* Brown, T., Hörsch, J., & Schlachtberger, D. (2017). PyPSA: Python for
  power system analysis. *arXiv Preprint arXiv:1707.09913*.
* Dunning, I., Huchette, J., & Lubin, M. (2017). JuMP: A modeling
  language for mathematical optimization. *SIAM Review*,
  *59*(2), 295–320.
* Fälth, H. E., Mattsson, N., Reichenberg, L., & Hedenus, F. (2023).
  Trade-offs between aggregated and turbine-level representations of
  hydropower in optimization models. *Renewable and Sustainable
  Energy Reviews*, *183*, 113406.
* Frysztacki, M. M., Hagenmeyer, V., & Brown, T. (2023). Inverse methods:
  How feasible are spatially low-resolved capacity expansion modelling
  results when disaggregated at high spatial resolution? *Energy*,
  *281*, 128133.
* Gong, C. C., Ueckerdt, F., Pietzcker, R., Odenweller, A., Schill, W.-P.,
  Kittel, M., & Luderer, G. (2023). Bidirectional coupling of the
  long-term integrated assessment model REgional model of INvestments and
  development (REMIND) v3. 0.0 with the hourly power sector model dispatch
  and investment evaluation tool with endogenous renewables (DIETER) v1.
  0.2. *Geoscientific Model Development*, *16*(17), 4977–5033.
* Gøtske, E. K., Pratama, Y., Andresen, G. B., Gidden, M. J., Victoria,
  M., & Zakeri, B. (2025). First steps towards bridging integrated
  assessment modeling and high-resolution energy system models: A scenario
  matrix for a low-emissions sector-coupled european energy system.
  *Environmental Research Communications*, *7*(8), 085010.
* He, G., Mallapragada, D., Macdonald, R., Law, J., Shaker, Y., Zhang, Y.,
  Cybulsky, A., Chakraborty, S., & Giovanniello, M. (2024).
  *DOLPHYN: Decision optimization for low-carbon power and hydrogen
  networks*. Github.
* Heo, T., & Macdonald, R. (2024). Effects of charging and discharging
  capabilities on trade-offs between model accuracy and computational
  efficiency in pumped thermal electricity storage. *arXiv Preprint
  arXiv:2411.07805*.
* Howells, M., Rogner, H., Strachan, N., Heaps, C., Huntington, H.,
  Kypreos, S., Hughes, A., Silveira, S., DeCarolis, J., Bazillian, M., &
  others. (2011). OSeMOSYS: The open source energy modeling system: An
  introduction to its ethos, structure and development. *Energy
  Policy*, *39*(10), 5850–5870.
* Hunter, K., Sreepathi, S., & DeCarolis, J. F. (2013). Modeling for
  insight using tools for energy model optimization and analysis (temoa).
  *Energy Economics*, *40*, 339–349.
* Jenkins, J. D., & Sepulveda, N. A. (2017). *Enhanced decision
  support for a changing electricity landscape: The GenX configurable
  electricity resource capacity expansion model*.
* Krishnan, V., & Cole, W. (2016). Evaluating the value of high spatial
  resolution in national capacity expansion models using ReEDS. *2016
  IEEE Power and Energy Society General Meeting (PESGM)*, 1–5.
* Levi, P. J., Kurland, S. D., Carbajales-Dale, M., Weyant, J. P., Brandt,
  A. R., & Benson, S. M. (2019). Macro-energy systems: Toward a new
  discipline. *Joule*, *3*(10), 2282–2286.
* Levin, T., Bistline, J., Sioshansi, R., Cole, W. J., Kwon, J., Burger,
  S. P., Crabtree, G. W., Jenkins, J. D., O’Neil, R., Korpås, M., &
  others. (2023). Energy storage solutions to decarbonize electricity
  through enhanced capacity expansion modelling. *Nature Energy*,
  *8*(11), 1199–1208.
* Levin, T., Blaisdell-Pijuan, P. L., Kwon, J., & Mann, W. N. (2024).
  High temporal resolution generation expansion planning for the clean
  energy transition. *Renewable and Sustainable Energy Transition*,
  *5*, 100072.
* Liu, B., Bissuel, C., Courtot, F., Gicquel, C., & Quadri, D. (2024). A
  generalized benders decomposition approach for the optimal design of a
  local multi-energy system. *European Journal of Operational
  Research*, *318*(1), 43–54.
* Loulou, R., Remme, U., Kanudia, A., Lehtila, A., & Goldstein, G.
  (2005). Documentation for the times model part ii. *Energy
  Technology Systems Analysis Programme*, *384*.
* Macdonald, R. (2024). *MacroEnergyScaling.jl*. Github.
* Macdonald, R., Pecci, F., Li, Anna, Lyu, R., & Atouife, M. (2025).
  *MacroEnergyExamples.jl*. Github.
* Mallapragada, D. S., Papageorgiou, D. J., Venkatesh, A., Lara, C. L., &
  Grossmann, I. E. (2018). Impact of model resolution on scenario outcomes
  for electricity sector system expansion. *Energy*, *163*,
  1231–1244.
* Odenweller, A., Ueckerdt, F., Hampp, J., Ramirez, I., Schreyer, F.,
  Hasse, R., Muessel, J., Gong, C. C., Pietzcker, R., Brown, T., &
  others. (2025). REMIND-PyPSA-eur: Integrating power system flexibility
  into sector-coupled energy transition pathways. *arXiv Preprint
  arXiv:2510.04388*.
* Parolin, F., Weng, Y., Colbertaldo, P., & Macdonald, R. (2025).
  Sectoral and spatial decomposition methods for multi-sector capacity
  expansion models. *arXiv Preprint arXiv:2504.08503*.
* Pecci, F., Bonaldo, L., & Jenkins, J. D. (2025).
  *MacroEnergySolvers.jl*. Github.
* Pecci, F., & Jenkins, J. D. (2025). Regularized benders decomposition
  for high performance capacity expansion models. *IEEE Transactions
  on Power Systems*.
* Pfenninger, S., & Pickering, B. (2018). Calliope: A multi-scale energy
  systems modelling framework. *Journal of Open Source Software*,
  *3*(29), 825.
* Qiu, L., Khorramfar, R., Amin, S., & Howland, M. F. (2024).
  Decarbonized energy system planning with high-resolution spatial
  representation of renewables lowers cost. *Cell Reports
  Sustainability*, *1*(12).
* Ruggles, T. H., Virgüez, E., Reich, N., Dowling, J., Bloomfield, H.,
  Antonini, E. G., Davis, S. J., Lewis, N. S., & Caldeira, K. (2024).
  Planning reliable wind-and solar-based electricity systems.
  *Advances in Applied Energy*, *15*, 100185.
* Ruhnau, O., & Qvist, S. (2022). Storage requirements in a 100%
  renewable electricity system: Extreme events and inter-annual
  variability. *Environmental Research Letters*, *17*(4),
  044018.
* Serpe, L., Cole, W., Sergi, B., Brown, M., Carag, V., & Karmakar, A.
  (2025). The importance of spatial resolution in large-scale, long-term
  planning models. *Applied Energy*, *385*, 125534.