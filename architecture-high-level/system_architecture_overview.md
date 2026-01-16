# System Architecture Overview

This document sketches the highest-level architecture of the conceptual Leviathan Swarm — a self-expanding asteroid mining and industrial system.

**Current status**: very early conceptual stage. No hardware exists. No detailed design exists. This is a whiteboard-level map to organize thinking and identify the biggest unknowns.

## Top-level subsystems

1. Seed / Bootstrap Layer  
   Purpose: Get from 0 → 1 self-expanding unit with minimal Earth mass & cost  
   Key elements:  
   - Jonesboro ground testbed (autonomy, superconductor synthesis, small-scale ISRU)  
   - Small number of initial modules (2–10 t total launch mass target)  
   - Electrostatic rail launch + chemical kick stage to LEO  
   - First NEA rendezvous & proof-of-replication loop closure  

2. Swarm Mining & Replication Core  
   Purpose: exponential mass growth via mining → refining → printing → replication  
   Key elements:  
   - Heterogeneous module types (drilling, processing, power, transport, replication)  
   - Uranus Ejector modules (trash → thrust + rogue management)  
   - Micro-satellite swarm for coordination, inspection, repair  
   - In-situ manufacturing (CNT structures, SiC shielding, superconductor coils)  
   - Mass-flow feedback loops (waste = propellant, product = more miners)

3. Power & Energy Backbone  
   Purpose: provide reliable, scalable power far beyond Earth supply chains  
   Key elements:  
   - Initial: compact fusion (10–15 MW/kg class)  
   - Mid-term: large 1.5 AU solar farm (CNT panels + superconductor bus)  
   - Long-term: beamed power, orbital solar concentrators, possible Dyson elements  
   - Superconductor interconnects (near-zero loss, high-current magnetic coils)

4. Orbital & Interplanetary Logistics Layer  
   Purpose: move mass & information efficiently across large distances  
   Key elements:  
   - Uranus Ejector high-Δv transport (10 km/s class, targeted ejection)  
   - Jupiter / Uranus gas scooping probes (H₂, N₂, CH₄ for propellant & atmosphere)  
   - Cyclers, momentum-exchange tethers, orbital depots (future)  
   - Laser / quantum comms backbone (1.5 AU hub relay)

5. Mars Terraforming & Surface Industrialization Layer  
   Purpose: turn Mars into a second industrial node with breathable atmosphere & magnetic protection  
   Key elements:  
   - Volatile delivery & vaporization (H₂O, CO₂ ejection)  
   - Core dynamo jumpstart (deep mining + laser heating + magnetic pulse)  
   - SiC greenhouse domes, ceramic hab construction, plant O₂ loops  
   - Superconductor-enabled magnetic coils for sustained dynamo

6. Rogue & Security Layer  
   Purpose: prevent single-unit failures from cascading into swarm collapse  
   Key elements:  
   - Uranus Probe micro-swarm for intercept / RTB / core-swap / containment  
   - QKD comms, blockchain consensus, thermite self-destruct  
   - Radiation-hardened AI, decentralized fault isolation

## Guiding architectural heuristics

- **Minimize Earth-sourced mass after seed phase** — everything after ~10 t should be made in space  
- **Waste = resource** — design so that 90%+ of mined mass becomes either product or propellant  
- **Swarm over monolith** — thousands of small, redundant units > one large fragile one  
- **Redundancy at every scale** — module-level, swarm-level, system-level  
- **Fail in place, fail safe** — rogues should be containable without destroying the swarm  
- **Bootstrap before optimize** — first loop closure > efficiency > elegance  

## Open architectural questions (2026)

- Minimum viable replication mass (1 kg? 10 kg? 100 kg?)  
- Best initial power source (fusion vs solar vs hybrid)  
- Reaction mass closure strategy (water vs CH₄ vs metal-oxygen vs tethers)  
- Rogue management scaling limit — how many Uranus Probes needed per million modules?  
- 1.5 AU solar farm mass payback time  
- Core dynamo energy requirement vs realistic heating volume  
- Single-point failure modes in the Jupiter/Uranus scooping loop  

This is deliberately incomplete.  
The point is to make the gaps visible so they can be filled.

Last updated: January 2026
