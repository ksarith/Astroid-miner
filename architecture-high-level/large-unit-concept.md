# Large von Neumann Unit Concept — “Leviathan Core”

## Overview

The **Large von Neumann Unit** (informally called a “Leviathan Core” or “asteroid eater”) is the high-end scale variant in the hybrid Leviathan Swarm architecture.

While the majority of the fleet consists of small, modular units (~10⁴ kg), this conceptual large unit is designed to internally consume and process an entire large asteroid (>1 km diameter, ~10¹² kg+ mass) in a self-contained way — eliminating most external swarm coordination for that target.

The name “Leviathan” finds its strongest expression here: one massive, self-sufficient processor that engulfs and refines an asteroid like a living thing.

## When It Makes Sense — The Threshold

Small swarm units excel on asteroids <100–300 m (~10⁶–10⁸ kg): they are flexible, redundant, low-risk, and easy to bootstrap.

Above ~1 km (~10¹² kg+), the coordination overhead of thousands of small units becomes a bottleneck:
- Communication latency and bandwidth limits
- Collision avoidance complexity
- Energy wasted moving material between distant units

At that scale, a single large unit that can land, anchor, enclose/crush, and process internally becomes more efficient despite higher upfront cost and complexity.

**Rough threshold rule of thumb** (subject to modeling):  
Large unit justified when asteroid recoverable mass × processing efficiency gain > cost of building & transporting the large unit.

## Proposed Internal Chamber Layout (multi-stomach model)

1. **Entry / Crushing Chamber**  
   - Anchor & initial enclosure (CNT tethers + inflatable SiC membrane)  
   - Laser or mechanical grinding to ~cm-scale particles (~0.1–1 m³/hour capacity)  
   - Goal: reduce asteroid to transportable chunks

2. **Volatile Extraction Chamber**  
   - Thermal processing (~600–900°C, laser or resistive heating, 10–100 kW)  
   - Volatiles driven off: H₂O (primary), CO₂, CH₄, NH₃, SO₂  
   - Cryogenic capture & storage (~20–100 K tanks)  
   - Expected yield: 5–30 wt% volatiles depending on asteroid type (C-type highest)  
   - Goal: fuel (H₂/O₂), life support gases, carbon feedstock

3. **Metal & Silicate Separation Chamber**  
   - Magnetic separation (Fe/Ni), electrostatic or centrifugal for silicates  
   - Slag rejection (non-useful rock ejected or stockpiled)  
   - Goal: high-purity metal ingots (~95% Fe/Ni recovery) + silicate powder for ceramics

4. **Fabrication Chamber (inert atmosphere)**  
   - Maintained in N₂ or Ar (sourced from volatiles or gas-giant scooping)  
   - 0g 3D printing / sintering of CNT frames, SiC components, DLC coatings, superconductor filaments  
   - Goal: produce new swarm units, GETM parts, or Ceres sphere segments

5. **Power & Compute Core**  
   - Central fusion reactor (~10–15 MW/kg class, TRL speculative)  
   - Quantum-dot AI cluster with ethical oversight layer  
   - Thermal management radiators + superconductor bus (193–200 K)  
   - Goal: self-power + decision-making for the entire unit

## Key Advantages vs. Small Swarm

- **Efficiency** — Internal material flow reduces transport losses & latency  
- **Control** — Tighter process optimization (e.g., 98% volatile recovery vs. 80–90% in distributed swarm)  
- **Scale** — Can process 10¹⁰–10¹² kg in months/years instead of years/decades  
- **Simplicity** — Fewer communication handoffs → lower error surface

## Key Disadvantages / Risks

- **Upfront cost** — Building & transporting a ~10⁹ kg unit is a major milestone  
- **Single point of failure** — If the large unit fails, loss is catastrophic (mitigated by redundancy & self-repair)  
- **Less flexible** — Poor for scattered small asteroids or precision work  
- **Ethical risk** — Larger unit = larger potential for misuse if safeguards fail (hence extra emphasis on kill switches, DAO consensus, transparency)

## Current Status

Purely conceptual — no prototypes exist.  
Next realistic step: ~1–10 m scale chamber mockup in lab or LEO (~$10k–$100k range) to test thermal volatile extraction + inert fab sequence.

Related files:  
- [CONCEPT.md](../CONCEPT.md) — hybrid philosophy  
- [module-getm.md](../module-getm.md) — high-thrust support unit  
- [safety-and-ethics.md](../safety-and-ethics.md) — why safeguards are non-negotiable

Open to feedback on chamber order, energy numbers, material flow rates, or anything that looks unrealistic.
