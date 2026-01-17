# Power Systems & Energy Scaling

**Repository Context**  
This document outlines the power architecture for the Leviathan self-replicating mining fleet, starting from near-Earth asteroids (NEAs, ~1–1.5 AU) and scaling to the main belt (~2–3.5 AU, e.g., Ceres at 2.8 AU). The focus is on **solar thermal as the primary stepping-stone** (easy in-situ fabrication, leverages asteroid metals/ceramics), with hybrids for reliability and eventual superconductor interconnects for orbital farms/rings. Energy is the critical bottleneck for mining, processing, replication, and long-term goals like Ceres planet-building.

**Core Principles**  
- Bootstrap with simple, producible tech (solar thermal tubes, Peltier/thermopiles) → transition to high-efficiency PV/superconductors as swarm replicates.  
- Prioritize scalability and ISRU: Use mined metals (Al, Cu) for coils/frames, silicates for ceramics, volatiles for electrolytes/cooling.  
- Sun-facing orientation + orbital rings for constant power (no night cycles).  
- Multi-use: Power mining/fabrication, AI processing, propulsion, and beamed energy (future orbital data centers or Earth sales).  
- No life-trampling: Clean, orbital/asteroid-based, minimal Earth dependency.

## 1. Solar Flux & Distance Scaling
Solar constant at 1 AU: ~1366 W/m²  
Effective collection efficiency (after losses): 15–40% depending on tech.

| Distance (AU) | Solar Flux (W/m²) | Approx. Power Density vs. 1 AU | Implications for Fleet |
|---------------|-------------------|--------------------------------|-------------------------|
| 1.0 (Earth/NEA) | 1366             | 100%                          | Baseline – high yield, solar thermal viable |
| 1.5 (Mars/outer NEA) | ~590          | ~43%                          | Still feasible; oversize arrays 2–3× |
| 2.0–2.5 (inner belt) | ~340–215     | 25–16%                        | Marginal for PV; thermal concentrators critical |
| 2.8 (Ceres)   | ~150             | ~11%                          | Requires large concentrators + nuclear backup |
| 3.5+ (outer belt) | <100          | <7%                           | RTG/fission dominant; solar supplemental |

**Scaling Strategy**  
- At 1–1.5 AU: Solar thermal backbone (tubes + concentrators) → 100–500 W/unit initially.  
- At 2+ AU: Deploy oversized parabolic mirrors (3D-printed from regolith) + hybrid RTG/nuclear for shadowed ops and high-demand tasks (melting, extrusion).  
- Long-term: Superconductor interconnects reduce transmission losses → enable large orbital solar farms around Ceres or NEAs.

## 2. Primary Power Technologies
### 2.1 Solar Thermal Stepping-Stone (Phase 1–2)
- **Why first?** Simple materials (aluminum/titanium tubes, ceramic cells), in-situ fab via centrifugal foundry + induction melting.  
- Components: Parabolic concentrators → heat pipes/tubes → working fluid (ammonia/water-glycol) → Peltier/thermopiles (5–10% heat-to-electricity) or direct heat for smelting.  
- Advantages: Direct thermal use (e.g., induction heaters, foundry ops) bypasses conversion losses.  
- Challenges: Thermal extremes, fluid management in zero-g (use wick structures/passive heat pipes), micrometeorite protection (regolith shielding).  
- Output target: 1–5 kW per mature unit (after replication cycles).

### 2.2 Photovoltaic (PV) Transition (Phase 2–3)
- High-efficiency GaAs cells (30–40%) for baseline electronics/AI.  
- In-situ fab: Silicon from rocky asteroids → thin-film deposition (harder than thermal tubes → delayed).  
- Deployable arrays (foldable/inflatable) for sun-tracking.

### 2.3 Nuclear Backup (Reliability Layer)
- RTGs (e.g., MMRTG ~110 W continuous) for shadowed ops, initial seed units.  
- Small fission reactors (1–10 kW) as swarm scales → in-situ shielding from asteroid metals.  
- Avoid dependency early; use only when solar flux drops below viability.

### 2.4 Orbital Solar Rings / Farms (Multi-Use Scaling)
- Pole-to-pole or equatorial rings in sun-synchronous orbits → constant sun exposure.  
- Multi-function: Energy beaming (microwaves/lasers), data processing (space-cooled AI farms), telescopes, telecom relays.  
- Earth variant: Bootstrap revenue → fund expansion.  
- Ceres variant: Local power hub for planet-building layers.  
- Superconductor interconnects: High-Tc materials synthesized under core pressure → lossless transmission.

## 3. Energy Budget per Replication Cycle
Rough estimates (adjust in notebooks):

- **Per unit cycle** (mining + fab + assembly): 1–10 MWh total (depends on induction melting, extrusion, welding).  
- **Breakdown**:
  - Collection/anchoring: 0.1–0.5 MWh  
  - Processing (induction + centrifugal): 0.5–5 MWh (dominant)  
  - AI/sensors/comms: 0.1–0.5 MWh  
  - Propulsion/delivery: variable (use mined propellants)  
- **Daily average demand** (mature swarm): 200–500 W baseline per unit → spikes to 1–10 kW during fab.  
- **Scaling rule**: Each replication doubles units but requires ~1.5–2× energy (efficiency gains from learning/swarm coordination).

See `notebooks/swarm_replication_growth.ipynb` for integrated energy-mass models.

## 4. Protection & Resilience
- **Thermal management**: Radiators + heat pipes/tubes; regolith burial for insulation/shielding.  
- **Radiation hardening**: Dormant spares, ECC memory, TMR processors.  
- **Debris mitigation**: Wide spacing, Uranus Ejector for controlled disposal.  
- **Redundancy**: Decentralized power nodes; modular arrays with failover.

## 5. References & Inspirations
- TransAstra / AstroForge concepts: Solar thermal for volatiles extraction and mining.  
- NASA ISRU roadmaps: Solar concentrators for asteroid processing.  
- Space-based solar power (SBSP): Orbital arrays, beamed energy (ESA SOLARIS, recent 2025–2026 demos).  
- Repo cross-links: `superconductor_interconnect_proposal.md`, `delta-v_and_reaction_mass_economy.md`.

**Next Steps**  
- Add notebook: `solar_flux_and_power_yield.ipynb` (AU-dependent calcs, concentrator sizing).  
- Model superconductor scaling for Ceres core.  
- Simulate ring deployment energy needs vs. replication rate.

Contributions welcome—fork, PR, or open issues!
