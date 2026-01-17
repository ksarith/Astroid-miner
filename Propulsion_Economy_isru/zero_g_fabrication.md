# Zero-G Fabrication

**Repository Context**  
This document details the challenges and proposed solutions for fabricating components in microgravity (zero-g / near-zero-g) environments as part of the Leviathan self-replicating asteroid mining fleet. Fabrication is one of the greatest hurdles for true autonomy: traditional Earth manufacturing relies heavily on gravity for settling, containment, material flow, and separation. In microgravity, molten metals form spheres due to surface tension, powders float, bubbles don't rise, and vibrations or forces can scatter material uncontrollably.

The goal is to enable in-situ production of structural parts, wire, tubes, coils, tools, and eventually complex components (e.g., processors, ceramics) using asteroid-derived resources (metals from M-types, silicates from rocky, volatiles from icy). All methods must be scalable, fabricable by earlier swarm generations, and compatible with the solar thermal stepping-stone power backbone.

## 1. Core Challenges in Zero-G Fabrication
- **Material Behavior**:
  - Molten metals/liquids: High surface tension → spherical droplets, pooling, or adhesion to surfaces.
  - Powders & particulates: Float freely → dust clouds, uneven deposition, contamination risk.
  - Gases/bubbles: Do not rise → trapped in melts, poor degassing.
- **Containment & Shape Control**:
  - No gravity to settle or press material → need artificial forces (centrifugal, electromagnetic, pressure).
  - Risk of cross-contamination between material types (e.g., Fe/Ni with silicates).
- **Thermal Management**:
  - Heat dissipation only via radiation → slow cooling, hot spots.
  - Thermal cycling stress on components.
- **Precision & Stability**:
  - Vibrations from mining/processing can misalign delicate operations (e.g., wire extrusion, welding).
  - Energy-intensive processes (melting, sintering) compete with swarm power budget.
- **Fleet Integration**:
  - Must bootstrap from simple seed capabilities → enable welders as primary fabricators.
  - Support downstream goals: wire for structures/superconductors, ceramics for cells, high-purity metals for electronics.

## 2. Key Fabrication Techniques & Solutions
| Technique                          | Primary Use Case                     | How It Works in Zero-G                              | Pros                                          | Cons                                          | Leviathan Fit & Your Ideas                     |
|------------------------------------|--------------------------------------|-----------------------------------------------------|-----------------------------------------------|-----------------------------------------------|------------------------------------------------|
| Centrifugal Foundry / Spinning Chamber | Melting, casting, extrusion, separation | Spin module (1–10 rpm) creates artificial gravity (~0.1–1 g) for settling, flow, and containment | Excellent containment; separates denser metals; enables extrusion | Mechanical complexity; bearing wear; energy for spin | Core idea: Centrifugal heads for wire extrusion; "stomach" chambers |
| Induction Heating + Electromagnetic Levitation | Melting, levitation, sorting         | Coils induce eddy currents → heat + levitate molten blobs | Contactless; no crucible contamination; dual-use for collection | Power-intensive; limited to conductors        | Induction heaters; eddy current inducers; conical ceramic heads |
| Conical Ceramic Head + Spun Extrusion | Continuous wire / filament production | Induction-heated ceramic die spins → centrifugal pressure extrudes molten metal into wire | Direct wire output; scalable; feed to welders | Cooling/quenching critical; adhesion risk     | Your conical heads with embedded coils; spool transport |
| Plasma / Magnetic Confinement Quenching | Rapid cooling of extrudate           | Ionized gas sheath held by magnetic field cools filament containerlessly | Fast quenching (~10–100 °C/s); prevents pooling | Plasma generation power; gas supply needed    | Magnetic-confined plasma sheath; fusion-inspired chamber |
| Radiative / Vacuum Cooling         | Simple solidification                | Rely on vacuum radiation + cold gas jets or shadows | No moving parts; low complexity               | Slow (~100–500 W/m² loss); shape control hard | Baseline for early stages; augment with radiators |
| Electroplating in Spinning Chamber | High-purity purification             | Centrifugal force drives electrolyte flow → uniform deposition | High purity for electronics/superconductors   | Electrolyte sourcing; energy use              | Reserved for critical metals; multi-chamber "stomach" |
| Laser / Optical Sintering          | Powder-based additive manufacturing  | Focused laser sinters regolith or metal powder layer-by-layer | Precision; works with rocky silicates         | Power-hungry; dust management                 | Future for ceramics/structures; test with solar concentrators |
| Welding as Primary Fabrication     | Structural assembly, repairs         | Laser, arc, or induction welding of extruded wire/parts | Versatile; enables complex shapes             | Requires feedstock (wire); heat-affected zones | Core fleet role: Welders build everything else |

**Precedents & Inspirations**:
- ISS experiments: Electromagnetic levitation of molten metals (containerless processing), fluid behavior in spinning modules.
- NASA ISRU concepts: Centrifugal casting for lunar/asteroid metal parts; optical sintering of regolith.
- AstroForge / TransAstra: Induction/plasma for asteroid metal extraction and vapor condensation.
- MIT microgravity extrusion: Hybrid wire + resin in zero-g (adaptable to pure metal with quenching).

## 3. Quenching & Solidification Strategies
Critical for wire/filament production to prevent deformation before spooling.

- **Plasma Sheath Quenching** (your preferred path):
  - Magnetic bottle (solenoid/Helmholtz coils) confines low-temperature plasma around extrudate.
  - High thermal conductivity gas (helium) convects heat away.
  - Axial field minimizes eddy interference with molten metal.
- **Inert Gas Jets**:
  - Directed pulses of mined argon/helium → convective cooling without ionization.
- **Radiative + Shadow Cooling**:
  - Extrude toward cold side of asteroid or through radiator fins.
- **Centrifugal Stretch & Thin-Filament Cooling**:
  - Spin faster during extrusion to draw thinner wire → larger surface area → faster radiative cooling.

## 4. Cross-Contamination & Purification Mitigation
- Selective induction: Only heats conductors → leaves silicates behind.
- Centrifugal separation: Denser metals sink → impurities float outward.
- Multi-chamber "stomach" sequence:
  1. Melt & initial separation
  2. Plasma arc/laser vaporization of volatiles/impurities
  3. Electroplating or magnetic levitation for final purity
- Uranus Ejector: Target non-useful material as waste or propellant.

## 5. Testing & Validation Roadmap
- **Ocean analogs**: Fluid dynamics, spin containment, quenching behavior under pressure/corrosion.
- **Parabolic flights / drop towers**: True microgravity for extrusion, levitation, plasma confinement.
- **LEO prototypes**: Small-scale induction + centrifugal modules on CubeSats or free-flyers.
- **NEA demos**: Seed units test full cycle before Ceres-scale ops.

## 6. References & Inspirations
- NASA: Containerless processing, centrifugal ISRU casting.
- AstroForge: Induction vaporization of asteroid simulants.
- Zero-g welding experiments (ISS): Electron beam & laser welding in vacuum.
- High-pressure synthesis tie-in: Future core layers for advanced ceramics/superconductors.

**Next Steps**  
- Notebook: `zero_g_fabrication_sim.ipynb` (centrifugal force calcs, cooling rates, extrusion dynamics).  
- Diagram: Process flow from collection → centrifugal melt → quenched wire → spool → welder.  
- Cross-link: `zero-g-collection-anchoring.md`, `induction_extrusion_sim.ipynb`, `power-solar-backbone/energy-scaling.md`.

Contributions welcome—fork, PR, or open issues!
