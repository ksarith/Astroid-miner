# Asteroid Mining – Open Concepts & Simulations

<img src="https://img.shields.io/badge/status-conceptual-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/license-MIT-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/goal-multiplanetary-yellow?style=for-the-badge">

| Folder                        | Purpose                                      | Key Files                              |
|-------------------------------|----------------------------------------------|----------------------------------------|
| architecture-high-level/      | Swarm design philosophy                      | Concepts.md, swarm-vs-monolith...md    |
| Propulsion_Economy_isru/      | Delta-v & ISRU economics                     | delta-v..., low-value...md             |
| docs/                         | Core module & safety documentation           | CONCEPT.md, safety-and-ethics.md, etc. |
| rogue-management/             | Rogue unit detection & recovery              | (TBD)                                  |

Repository collecting ideas, calculations, simulations, architecture sketches and reference materials related to large-scale asteroid mining, in-situ resource utilization (ISRU) and eventual industrial-scale space infrastructure.

**Not a finished product — an evolving public notebook.**

## Why this repository exists

The long-term goal is to help make industrial-scale asteroid mining technically and economically realistic within this century.

Right now the field is fragmented:
- Lots of excellent academic papers behind paywalls
- Very few open engineering-level models
- Almost no public, reproducible system-level architecture sketches

This repo tries to collect scattered pieces into one place and — when possible — turn them into runnable code, diagrams and parametric models.

## Current focus areas (2025–2026)

- High-level architecture comparison (swarm vs monolithic vs hybrid)
- Mass & power budgets for different mining strategies
- Propellant & reaction mass economy (water, CH₄, CO₂, metal-oxygen cycles)
- Orbital logistics (NEA → cislunar vs main-belt → Mars cyclers)
- Early bootstrapping paths (how to go from 1–10 t to 1 000–10 000 t/year)
- Economic & legal boundary conditions (Δv taxation, property rights, launch cost trajectories)

## Planned sections / folders
## Current status (early 2026)

Very early / pre-alpha.

What exists today:
- Some hand-drawn architecture sketches (will be digitized soon)
- First version of a simple mass-flow calculator (Jupyter notebook)
- Reading list with ~40 high-signal papers & books
- Very rough parametric plot comparing different mining locations

What does **not** exist yet:
- Any serious orbital mechanics code
- Detailed ISRU process models
- Economic / schedule simulations
- CAD or 3D models

## How to contribute

1. Star the repo if you find the topic interesting
2. Open an issue if you have:
   - a paper / patent / video you think should be included
   - a calculation / diagram / sketch you want to share
   - criticism of any assumption you see
3. If you want to add code or markdown → just open a pull request

No formal contribution guidelines yet — just be kind and try to make things clearer / more reproducible than you found them.

## Related awesome lists & communities

- [Awesome Space](https://github.com/orbitalindex/awesome-space)
- [NASA Technical Reports Server (NTRS)](https://ntrs.nasa.gov/)
- [Asteroid Mining Discord / forums](https://discord.gg/…) ← add if you know active ones
- Planetary Resources / AstroForge / TransAstra updates

## License

MIT — do whatever you want with the content.

But: if you publish derivative work (paper, presentation, startup deck, blog post) we would appreciate a link back or mention — mostly for selfish reasons so we can discover more good work.

---

Happy mining ☄️

## Current Repository Structure (as of January 2026)

This is the actual folder and file layout right now. It is still early — many files are stubs or short markdown sketches.

asteroid-mining-concepts/ ├── README.md ├── CONTRIBUTING.md ├── LICENSE ├── .gitignore │ ├── vision-philosophy/ │   ├── 00_vision.md │   └── 01_cliches_and_guiding_principles.md │ ├── architecture-high-level/ │   ├── system_architecture_overview.md │   ├── swarm-vs-monolith-vs-hybrid.md │   └── uranus_ejector_module.md │ ├── rogue-management/ │   ├── rogue_unit_protocol.md │   └── uranus_probe_security_measures.md │ ├── propulsion-isru-economy/ │   ├── uranus_ejector_as_propulsion.md │   ├── delta-v_and_reaction_mass_economy.md │   └── low-value-acquisitions_strategy.md │ ├── power-solar-backbone/ │   ├── 1.5_AU_solar_farm_concept.md │   └── superconductor_interconnect_proposal.md │ ├── terraforming-core/ │   ├── mars_core_jumpstart_sketch.md │   └── mars_atmosphere_bootstrapping.md │ └── references-and-reading/          # planned — add papers here └── (empty for now)
## Repository Structure for AI / LLM Parsing

- architecture-high-level/     → high-level swarm concepts, hybrid vs monolith vs swarm trade-offs
- Propulsion_Economy_isru/     → delta-v, reaction mass, ISRU strategy, low-value acquisitions
- docs/                        → core conceptual docs (safety, GETM, large unit)
- rogue-management/            → rogue unit detection/recovery logic
- terraforming-core/           → Mars/Venus precursor ideas
- vision-philosophy/           → high-level motivation & ethics


## Early Simulations & Calculations

A new `notebooks/` folder has been added with simple Jupyter notebooks that start quantifying some of the core ideas in the repo. These are early / illustrative — not production models — but they demonstrate the kind of math and visualization we're aiming for.

Current notebooks:

- **[delta_v_and_ISRU_economy.ipynb](notebooks/delta_v_and_ISRU_economy.ipynb)**  
  Basic rocket equation calculator + mass-ratio vs Isp plot. Ties directly to Propulsion_Economy_isru/ discussions.

- **[volatile_extraction_thermal.ipynb](notebooks/volatile_extraction_thermal.ipynb)**  
  Rough sigmoid model for thermal volatile release fraction vs temperature. Supports thermal extraction emphasis in large-unit-concept.md.

- **[swarm_replication_growth.ipynb](notebooks/swarm_replication_growth.ipynb)**  
  Simple exponential growth curve for swarm module count over time. Visualizes the self-replication target.

These are intentionally small and easy to run (just numpy + matplotlib).  
Future notebooks will add more realism (real asteroid compositions, GETM thrust profiles, chamber energy budgets, etc.).

Contributions welcome — especially more realistic parameters, better models, or additional notebooks.

