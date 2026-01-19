# Astroid-miner

## Repository Structure & File List

### Root
- [CONTRIBUTING.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/CONTRIBUTING.md) – Contribution guidelines
- [README.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/README.md) – This file

### architecture-high-level/
High-level system design, swarm philosophy, stability, ejector modules.

- [Concepts.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/architecture-high-level/Concepts.md) – Core conceptual overview
- [swarm-vs-monolith-vs-hybrid.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/architecture-high-level/swarm-vs-monolith-vs-hybrid.md) – Swarm vs monolithic vs hybrid architectures
- [zero-spheres-stability.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/architecture-high-level/zero-spheres-stability.md) – Stability for spherical structures
- [uranus_ejector_module.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/architecture-high-level/uranus_ejector_module.md) – Uranus Ejector module design
- [system_architecture_overview.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/architecture-high-level/system_architecture_overview.md) – Overall system architecture summary
- [large-unit-concept.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/architecture-high-level/large-unit-concept.md) – Concept for large-scale "monster" units

### Propulsion_Economy_isru/
Delta-v budgets, reaction mass loops, low-value strategy, zero-g ops, Uranus Ejector as propulsion.

- [delta-v_and_reaction_mass_economy.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/Propulsion_Economy_isru/delta-v_and_reaction_mass_economy.md) – Delta-v and reaction mass economy
- [low-value-acquisitions_strategy.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/Propulsion_Economy_isru/low-value-acquisitions_strategy.md) – Low-value resource prioritization
- [module-getm.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/Propulsion_Economy_isru/module-getm.md) – GETM (Gas Extraction & Thrust Module)
- [uranus_ejector_as_propulsion.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/Propulsion_Economy_isru/uranus_ejector_as_propulsion.md) – Uranus Ejector repurposed for propulsion
- [zero-g-collection-anchoring.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/Propulsion_Economy_isru/zero-g-collection-anchoring.md) – Zero-g collection and anchoring methods
- [zero_g_fabrication.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/Propulsion_Economy_isru/zero_g_fabrication.md) – Zero-g fabrication techniques

### notebooks/
Simulation notebooks and early thought logs.

- [delta_v_and_ISRU_economy.ipynb](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/notebooks/delta_v_and_ISRU_economy.ipynb) – Delta-v and ISRU economy modeling
- [swarm_replication_growth.ipynb](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/notebooks/swarm_replication_growth.ipynb) – Swarm replication growth simulation 
- [volatile_extraction_thermal.ipynb](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/notebooks/volatile_extraction_thermal.ipynb) – Thermal volatiles extraction modeling
- Astroid Mining.txt
- Astroid Mining2.txt
- Astroid Mining3.txt

### power-solar-backbone/
Solar thermal backbone, energy scaling, superconductor proposals, orbital farm concepts.

- [energy-scaling.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/power-solar-backbone/energy-scaling.md) – Energy scaling across AU distances
- [superconductor_interconnect_proposal.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/power-solar-backbone/superconductor_interconnect_proposal.md) – Proposal for superconductor interconnects
- [1.5_AU_solar_farm_concept.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/power-solar-backbone/1.5_AU_solar_farm_concept.md) – Solar farm concept at 1.5 AU

### terraforming-core/
Ceres and Mars terraforming / planet-building sketches.

- [ceres-planet-building.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/terraforming-core/ceres-planet-building.md) – Ceres as planet-building seed
- [mars_core_jumpstart_sketch.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/terraforming-core/mars_core_jumpstart_sketch.md) – Mars core jumpstart sketch
- [mars_atmosphere_bootstrapping.md](https://raw.githubusercontent.com/ksarith/Astroid-miner/main/terraforming-core/mars_atmosphere_bootstrapping.md) – Mars atmosphere bootstrapping concepts

# Discovery — Project Map & Raw Links

This file is the **canonical index** for the Astroid-miner repository.

Its purpose is to:
- Provide a **stable project map**
- Expose **raw file links** for AI ingestion
- Reduce navigation friction for humans
- Avoid duplication of content found elsewhere

If a document exists in the repository, it should be reachable from here.

---

## Project Overview

Astroid-miner explores concepts, architectures, and constraints around:
- Industrial-scale asteroid mining
- In-situ resource utilization (ISRU)
- Self-expanding off-world industrial systems
- Long-horizon autonomy with strict ethical bounds

This repository focuses on **mining, fabrication, and replication logic**.  
Closely related ethical and systems work exists in the Lazarus Forge project (linked below).

---

## Vision & Philosophy (Canonical)

High-level intent, ethics, and long-term framing.

- **Vision**  
  https://raw.githubusercontent.com/ksarith/Astroid-miner/refs/heads/main/vision-philosophy/Vision.md

- **Ethical AI Frameworks**  
  https://raw.githubusercontent.com/ksarith/Astroid-miner/refs/heads/main/vision-philosophy/Ethical_AI_Frameworks.md

- **Self-Evolving AI**  
  https://raw.githubusercontent.com/ksarith/Astroid-miner/refs/heads/main/vision-philosophy/Self-Evolving_AI.md

- **Rogue Unit Management (Preservation-First)**  
  https://raw.githubusercontent.com/ksarith/Astroid-miner/refs/heads/main/vision-philosophy/Rogue_unit_management.md

---

## Architecture & Technical Exploration

System layouts, trade studies, and early technical reasoning.

- **Iterative R&D & Prototyping (condensed concepts)**  
  https://raw.githubusercontent.com/ksarith/Astroid-miner/refs/heads/main/vision-philosophy/iterative-rd-prototypes.md

(Additional architecture and subsystem documents will appear here as they mature.)

---

## Safety & Ethics (Operational)

Safety constraints that apply across all subsystems.

- **Safety and Ethics**  
  https://raw.githubusercontent.com/ksarith/Astroid-miner/refs/heads/main/vision-philosophy/SAFETY-AND-ETHICS.md

---

## Cross-Project Reference — Lazarus Forge

Lazarus Forge explores **broader autonomous industrial systems**, governance, and AI-centric fabrication logic that overlap with Astroid-miner.

- **Lazarus Forge — Project Map & Raw Links**  
  https://raw.githubusercontent.com/ksarith/Lazarus-Forge-/main/Discovery.md

Astroid-miner can be considered a **domain-specific sibling** focused on asteroid mining and ISRU.

---

## Notes on Structure

- This file intentionally contains **no analysis or philosophy**
- It should change **rarely**
- Documents may evolve, but links here should remain valid
- Deprecated or merged files should be removed from this index

If a link here is broken, it should be fixed immediately.

---

Last updated: January 2026
