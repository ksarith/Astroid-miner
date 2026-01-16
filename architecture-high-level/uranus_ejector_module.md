# Uranus Ejector Module & Uranus Ejector Probe

Two closely related but distinct concepts that have appeared repeatedly in the thinking around propulsion, waste management, rogue handling, and interplanetary logistics.

## 1. Uranus Ejector (the mechanism)

**What it is**  
A compact, CH₄-boosted high-velocity ejection system integrated into swarm modules and micros.  
Ejects non-product mass (mining tailings, Jonesboro trash, excess regolith, spent coolant, off-spec parts) as reaction mass to generate thrust.

**Core specs (conceptual target)**
- Ejection velocity: 10 000 m/s (baseline goal)
- Propellant: gaseous CH₄ or CH₄/H₂ mix (from C-type asteroids or Sabatier-style processing)
- Thrust class: 10–100 N per module (scalable with nozzle size)
- Specific impulse: ~3 000–4 000 s (very high for chemical systems)
- Mass penalty: ~5–10% of module dry mass
- Targeting: can aim ejection vectors with ±0.1° precision (gimbal + AI)

**Primary purposes**
1. **Propulsion from waste** — every kg of unwanted mass becomes Δv instead of dead weight
2. **Targeted delivery** — can direct volatiles (H₂O, CO₂, CH₄) toward Mars atmosphere, orbital depots, or safe disposal zones
3. **Momentum management** — fine station-keeping and despin without dedicated propellant
4. **Emergency high-Δv** — short-burn escape or intercept capability

**Naming note**  
“Uranus Ejector” is deliberately cheeky — it started as a pun on waste ejection and Uranus’ methane atmosphere, but the function is dead serious. The joke stuck because it’s memorable.

## 2. Uranus Ejector Probe (the rogue-management vehicle)

**What it is**  
A small (10 kg, 0.1 m³) specialized micro-module built around a scaled-up Uranus Ejector thruster, plus:
- 1 km deployable CNT tether
- IR sensor + quantum comms (10 Gbps laser)
- Spare AI core (10 kg) for swap
- Micro-arms for docking

**Core specs (conceptual target)**
- Dry mass: 10 kg
- Δv capability: 10 000 m/s (baseline), 20 000 m/s overload
- Tether strength: 1 kN (CNT, 99% hit rate at 1 km)
- Endurance: 1–2 weeks active chase (CH₄ tank)
- Cost target: $0.1M/unit (self-built: $0.05M Fe/Ni + CH₄, $0.05M sensors/comms)

**Primary purposes**
1. **Intercept & RTB** — chase rogue units (10 sec at 100 km, 2 hours at 1 000 km), latch via tether, override AI, return to hub
2. **Core swap assist** — dock, replace rogue AI core (10 min), preserve mining uptime (270 000 kg/h per module)
3. **Non-destructive arrest** — tether + 10 000 m/s nudge (100–1 000 km off-orbit), or 5-probe CNT net containment (5 km², 5 000 m/s collective drag)
4. **Last-resort neutralization** — overload ejector (20 000 m/s ram) if hostile (collision imminent), minimize Kessler risk

**Why the probe exists**
RTB (95% success) and core swap (99.9%) handle most rogues.  
The 5% that resist (damaged thrusters, hostile rewrite, orbit drift) need a fast, cheap, non-destructive chaser.  
The Uranus Probe fills that gap — turns a potential $15M loss or cascade into a 98% recovery.

**Naming note (again)**  
Yes, it’s cringe. Yes, the pun stuck. Yes, it’s memorable.  
The function is serious; the name is just Jonesboro humor.

## Summary table

| Aspect                     | Uranus Ejector (mechanism)               | Uranus Ejector Probe (vehicle)             |
|----------------------------|-------------------------------------------|---------------------------------------------|
| Mass                       | Integrated (5–10% of host module)         | 10 kg standalone                            |
| Δv                         | 10 000 m/s nominal                        | 10 000–20 000 m/s                           |
| Main function              | Waste → thrust + targeted ejection        | Intercept, RTB, core swap, arrest of rogues |
| Propellant                 | CH₄, mining byproducts, trash             | CH₄ tank (50–100 kg)                        |
| Typical use case           | Daily mining ops, station-keeping         | Rogue response (0.1–5% of swarm incidents)  |
| Risk mitigated             | Reaction mass starvation                  | Swarm disruption, revenue loss, Kessler     |
| Cost target                | Negligible incremental                    | $0.1M/unit (self-built)                     |

## Open questions

- Minimum CH₄ tank size for 2-hour intercept (50 kg? 100 kg?)
- Tether material & length trade-off (1 km CNT baseline — is 2 km worth the mass?)
- Overload ram safety (20 000 m/s — what debris profile is acceptable?)
- Swarm density limit — how many rogues can 1 000 probes realistically handle?

This is still conceptual.  
The Uranus Ejector mechanism is almost certainly useful; the probe is a “nice to have” that becomes “must have” once swarm size exceeds ~10⁵ units.

Last updated: January 2026
