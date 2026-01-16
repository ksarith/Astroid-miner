# Superconductor Interconnect Proposal

The backbone of the 1.5 AU solar farm (and eventually the entire swarm) relies on near-zero-loss power & data transmission at multi-TW scale.

This document sketches the current thinking around using high-temperature superconductors (specifically the Cu-La-S-B-H-C-N family) as the interconnect material.

## Why superconductors at all

At gigawatt-to-terawatt scales:
- Resistive losses in copper become unacceptable (even at 1% loss → 10–100 GW heat to radiate)
- Conventional cryocooling (LN₂ at 77 K) adds massive mass & complexity
- We need a material that operates at or near Mars ambient temperatures (~–80°C / 193 K shade side) without active refrigeration

Goal: 193–210 K operation, zero resistive loss, high current density, manufacturable in situ from asteroid resources.

## Current candidate: Cu-La-S-B-H-C-N filament

**Synthesis method (baseline)**
- Substrate: Cu filament (~0.1 mm) or CNT-dominant (~0.1 μm Cu-S-H seed)
- Bath: NH₃ (10 bar, 5°C, N₂ atmosphere)
- Additives: LaCl₃ (0.02 M), (NH₄)₂S (0.15 M), urea (0.1 M), BCl₃ (0.01 M), NH₄OH (0.1 M), NH₄Cl (0.1 M), CNTs (~2 wt%)
- Deposition: Pulsed DC (0.1 V, 0.01 A), 0.3 T magnetoelectrolysis
- Shell: 1–5 μm thick with ~1.5–1.9 Å channels
- Dopants: La (~2 at%), S (~6 at%), B (~2 at%), H (~5 at%), C-N (~2 at%)
- Post-synthesis: 0.1 GPa H₂ anneal (200°C)
- Encapsulation: Double CNT (~2 μm) + graphene (~0.1 μm) + Sn (~1 μm) for H retention (~10⁻¹² cm²/s)

**Test conditions**
- Vacuum: 10⁻⁶ torr
- Temperature ramp: –195°C → –80°C
- Current: 0.01–1 A
- Result: Zero resistance observed at 193 K (–80°C)

## Target performance (aspirational)

| Property                   | Current (2026)       | Mid-term goal (2035) | Long-term goal (2050+) |
|----------------------------|----------------------|----------------------|------------------------|
| Tc (critical temp)         | 193 K                | 200–210 K            | 220–250 K              |
| Operating range            | –195°C to –80°C      | –150°C to –50°C      | –100°C to 0°C          |
| Critical current density   | TBD                  | >10⁶ A/cm²           | >10⁷ A/cm²             |
| Mass per meter             | ~0.1 g/m             | ~0.05 g/m            | ~0.02 g/m              |
| Magnetic field tolerance   | 0.3 T (deposition)   | 5–10 T               | 20–50 T                |
| H retention                | 10⁻¹² cm²/s          | 10⁻¹³ cm²/s          | 10⁻¹⁴ cm²/s            |
| In-situ manufacturability  | Lab bath             | NEA/C-type reactor   | Fully autonomous       |

## Applications in the swarm

1. **Solar farm bus**  
   - Connects 10¹²–10¹⁴ m² panels into TW-scale ring/spoke topology  
   - Zero resistive loss → no active cooling needed on shade side

2. **Magnetic pulse coils**  
   - 10 T coils for Mars core dynamo jumpstart (10²⁰–10²² J pulses)  
   - Enables 0.1 G field generation without gigawatt-scale resistive heating

3. **Power distribution**  
   - Feeds TW from solar farm to Mars surface, orbital habs, propulsion depots  
   - Enables beamed-power demos (future)

4. **High-speed data & compute interconnect**  
   - Super-low-loss links for 10²⁰–10²² flops swarm coordination  
   - Reduces latency & power for AI consensus & rogue detection

## Manufacturing path

- **Seed phase**: Earth/Jonesboro lab synthesis (NH₃ bath, pulsed DC, 0.3 T field)
- **Bootstrap phase**: In-orbit / NEA reactors (0.1 GPa H₂ anneal, CNT feedstock)
- **Exponential phase**: Fully autonomous printers using asteroid Cu, S, La, B, C, N sources

## Open questions

- Realistic Tc ceiling for this chemistry family (210 K? 220 K?)
- Critical current density at 5–10 T fields
- Mass penalty of encapsulation vs plain filament trade-off
- Degradation rate under cosmic radiation & thermal cycling
- Scalable synthesis reactor design (pressure vessel mass vs output)
- How to test 10 T coils at scale without destroying the test article

This is still early conceptual work.  
The 193 K result is promising but needs independent replication and scaling studies.

Last updated: January 2026
