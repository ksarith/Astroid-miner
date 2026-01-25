# Astroid-miner – Repository Discovery Map

This file provides a complete overview of the current repository structure with direct links to every document.

## Root
- [CONTRIBUTING.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/CONTRIBUTING.md) – Contribution guidelines
- [README.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/README.md) – Project overview
- [Discovery.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/Discovery.md) – This file

## architecture-high-level/
High-level system design, swarm philosophy, stability, ejector modules.

- [Concepts.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/architecture-high-level/Concepts.md) – Core conceptual overview
- [swarm-vs-monolith-vs-hybrid.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/architecture-high-level/swarm-vs-monolith-vs-hybrid.md) – Swarm vs monolithic vs hybrid architectures
- [zero-spheres-stability.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/architecture-high-level/zero-spheres-stability.md) – Stability for spherical structures
- [uranus_ejector_module.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/architecture-high-level/uranus_ejector_module.md) – Uranus Ejector module design
- [system_architecture_overview.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/architecture-high-level/system_architecture_overview.md) – Overall system architecture summary
- [system redundancy](https://raw.githubusercontent.com/ksarith/Astroid-miner/refs/heads/main/architecture-high-level/Fault-Tolerant-Power-Control.md) - Fault tolerance systems
- [Roles of Units](https://raw.githubusercontent.com/ksarith/Astroid-miner/refs/heads/main/architecture-high-level/Roles_Doctrine.md) - Defining generalized units as core key for success.


## Propulsion_Economy_isru/
Delta-v budgets, reaction mass loops, low-value strategy, zero-g ops, Uranus Ejector as propulsion.
- [Magnetic Drive](https://raw.githubusercontent.com/ksarith/Astroid-miner/refs/heads/main/Propulsion_Economy_isru/Magnetic_Drive.md) - proposed thrust mechanism
- [low-value-acquisitions_strategy.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/Propulsion_Economy_isru/low-value-acquisitions_strategy.md) – Low-value resource prioritization
- [module-getm.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/Propulsion_Economy_isru/module-getm.md) – GETM (Gas Extraction & Thrust Module)
- [zero-g-collection-anchoring.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/Propulsion_Economy_isru/zero-g-collection-anchoring.md) – Zero-g collection and anchoring methods
- [zero_g_fabrication.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/Propulsion_Economy_isru/zero_g_fabrication.md) – Zero-g fabrication techniques

## notebooks/
Simulation notebooks and early thought logs.  

- Deleted Jupyter notes: still too early
- Astroid Mining.txt
- Astroid Mining2.txt
- Astroid Mining3.txt

## power-solar-backbone/
Solar thermal backbone, energy scaling, superconductor proposals, orbital farm concepts.

- [energy-scaling.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/power-solar-backbone/energy-scaling.md) – Energy scaling across AU distances
- [superconductor_interconnect_proposal.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/power-solar-backbone/superconductor_interconnect_proposal.md) – Proposal for superconductor interconnects
- [1.5_AU_solar_farm_concept.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/power-solar-backbone/1.5_AU_solar_farm_concept.md) – Solar farm concept at 1.5 AU
  

## terraforming-core/
Ceres and Mars terraforming / planet-building sketches.

- [Martian atmosphere](https://raw.githubusercontent.com/ksarith/Astroid-miner/refs/heads/main/terraforming-core/Martian_Atmosphere.md) 
- [ceres-planet-building.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/terraforming-core/ceres-planet-building.md) – Ceres as planet-building seed
- [Ceres refining](https://raw.githubusercontent.com/ksarith/Astroid-miner/refs/heads/main/terraforming-core/ceres_metabolic_nucleus.md) - expanding Ceres planet-building ideology
- [mars_core_jumpstart_sketch.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/terraforming-core/mars_core_jumpstart_sketch.md) – Mars core jumpstart sketch
- [mars_atmosphere_bootstrapping.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/terraforming-core/mars_atmosphere_bootstrapping.md) – Mars atmosphere bootstrapping concepts
- [How to put planets in their place](https://raw.githubusercontent.com/ksarith/Astroid-miner/refs/heads/main/terraforming-core/planetary_orbital_conditioning.md)

## vision-philosophy/
Guiding principles, self-evolving AI, ethical frameworks, safety commitments.

- [Vision.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/vision-philosophy/Vision.md) – Overall vision and long-term horizon
- [self-evolving-ai.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/vision-philosophy/self-evolving-ai.md) – Self-evolving AI design and safeguards
- [ethical-ai-frameworks.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/vision-philosophy/ethical-ai-frameworks.md) – Ethical AI frameworks and boundaries
- [Rogue Unit Management](https://raw.githubusercontent.com/ksarith/Astroid-miner/refs/heads/main/vision-philosophy/Rogue_unit_management.md)
- [Safety Lights](https://raw.githubusercontent.com/ksarith/Astroid-miner/refs/heads/main/vision-philosophy/Safety_Lights.md) - mundane and fundamentally boring
- [Interstellar Seeding Doctrine](https://raw.githubusercontent.com/ksarith/Astroid-miner/refs/heads/main/vision-philosophy/Interstellar_Seeding.md) - How and when to leave our Solar System


## Notes on Swarm Notebooks
- Git command (locally): `git rm notebooks/Swarm_replication_growth.ipynb` then commit/push.
- Update any internal links to point to the kept file.

## Next Steps / Planned
- Consider adding `docs/` or `zero-g-challenges/` folder for better organization
- Expand notebooks: power scaling, quenching sims, more delta-v models
- Create visual diagrams (swarm growth, Ceres layering, Uranus Ejector flow diagram)
- Benchmark against real-world efforts (AstroForge, TransAstra, NASA ISRU studies)

Open issues, PRs, and discussions are very welcome.  
This is an evolving, collaborative exploration of self-sustaining asteroid mining and far beyond.

**Last major update:** January 19, 2026

---

## Cross-Project Reference — Lazarus Forge

Lazarus Forge explores **broader autonomous industrial systems**, governance, and AI-centric fabrication logic that overlap with Astroid-miner.

Project map & raw links: [Lazarus Forge Discovery.md](https://raw.githubusercontent.com/ksarith/Lazarus-Forge-/main/Discovery.md)
Project map & raw links: [Astroid-miner Discovery.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/refs/heads/main/Discovery.md)
