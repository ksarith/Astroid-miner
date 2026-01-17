# GETM — Gas Extraction & Thrust Module

**Primary role**  
High-thrust propulsion and gas-resource extraction from outer-planet atmospheres (Uranus, Jupiter, etc.) to support fleet fuel production, material transport, and long-range logistics.

**Secondary / bonus capability**  
When mission parameters allow, precise trajectory targeting and material ejection (coilgun, 10⁴ m/s) for terraforming precursor delivery or orbital construction supply.

**Tertiary capability**  
Rogue-unit recovery: probe, intercept, and physically disable/capture non-compliant swarm members (0.1% risk mitigation).

## Design Rationale

- Thrust-first design maximizes Δv and mission velocity → faster bootstrapping of distant operations (5–19 AU).  
- Scooping is secondary because high-thrust transit is the bigger bottleneck for outer-system scaling.  
- Rogue recovery is tertiary because it is a low-probability but high-consequence safety requirement.  
- All capabilities gated behind ethical AI checks to maintain peaceful-use-only posture.

## Current Proposed Specifications (concept stage — January 2026)

| Category               | Specification                                      | Notes / Status                          |
|------------------------|----------------------------------------------------|-----------------------------------------|
| **Mass**               | ~5,000 kg                                          | Reduced from earlier 10⁴ kg for thrust efficiency |
| **Dimensions**         | 4 m × 1.5 m × 1.5 m                                | Streamlined for high-velocity transit   |
| **Hull / Shielding**   | CNT-graphene composite (~100 GPa) + SiC multilayer (5 mm) | 98% heat resistance @ 1,500°C, radiation hardening for ~0.1 R/h (Uranus) |
| **Primary Propulsion** | Fusion plasma thrusters (~10.5 MW/kg, ~10⁴ N thrust) | Δv target 10,000 m/s, H₂ fuel from scooping |
| **Secondary Propulsion** | Hall-effect ion thrusters (~40 km/s Δv, ~10⁻³ m/s²) | Efficiency mode, limits weaponization potential |
| **Power**              | Compact fusion reactor (~50 W, 99.5% uptime) + CNT solar backup (~100 W/m² @ 19 AU, 5 m²) | Superconductor bus (193 K) for 0% loss |
| **Scooping**           | CNT-diamond scoops (~5 m²) + cryogenic tanks (~20 K) | ~10 kg/day H₂/He-3 at ~15 km/s relative velocity |
| **Processing**         | Magneto-centrifugal gas separator                  | H₂ ~90%, He-3 ~0.001%, ~1 kg/day stored |
| **Ejection (bonus)**   | Electromagnetic coilgun (superconductor coils, 0.3 T) | 10⁴ m/s, ~5 kg payload, 98% efficiency |
| **Rogue Recovery**     | LIDAR (10 m resolution) + CNT grappling arms (~100 N) | Autonomous intercept & disable sequence |
| **Compute**            | Quantum-dot AI nodes (~10¹³ flops/W)               | Neuroevolution (NEAT) + RL + ethical reward shaping |
| **Ethical / Safety**   | Asimov laws, DAO consensus (80–99%), anomaly detection (99.9%), thermal kill switches (>200 K) | Transparency via public telemetry |
| **Comms**              | Laser (10⁸ bits/s, superconductor) + radio backup  | 5 AU range, AI compression (95%) |
| **Environmental**      | Operates ~76 K (Uranus), radiation ~0.1 R/h, micrometeorite flux ~10⁻⁴/m²/year | SiC-CNT shielding, self-healing CNT layers |
| **Unit count (planned)** | 50 units                                           | ~$15M total, offset by ~$20M H₂O/H₂ sales |

## Key Open Questions

- Fusion maturity timeline (10.5 MW/kg realistic by 2030–2035?)  
- Realistic scooping yield at Uranus wind speeds (~250 m/s) and low density  
- Radiation hardening cost/benefit trade-off vs. Jupiter (~10 R/h)  
- Rogue recovery success probability in high-relative-velocity intercepts  
- Ethical-AI false-positive rate when gating high-thrust modes

## Related Files

- [safety-and-ethics.md](../safety-and-ethics.md) — full anti-weaponization rationale  
- [CONCEPT.md](../CONCEPT.md) — hybrid small/large unit philosophy  
- [large-unit-concept.md](../large-unit-concept.md) — asteroid-consuming “monster” variant

Feedback and realism checks very welcome — Issues or Discussions preferred.
