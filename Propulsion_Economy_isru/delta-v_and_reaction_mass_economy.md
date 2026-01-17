# Delta-V & Reaction Mass Economy

How the swarm pays for its own mobility at scale.

## Guiding principle

After the first replication loop closes, **no net mass leaves the system except as useful product or intentional exhaust**.  
Every kg of mined material must become either:
- Structure (CNT/SiC modules, solar panels, habs)
- Product (Fe/Ni, volatiles for Mars)
- Propellant / reaction mass

## Main reaction mass cycles considered

| Cycle                     | Propellant / exhaust        | Isp range (s) | Source material               | Advantages                              | Disadvantages                          |
|---------------------------|-----------------------------|---------------|-------------------------------|-----------------------------------------|----------------------------------------|
| Uranus Ejector (baseline) | CH₄, H₂O dissoc., CO₂       | 3 000–4 500   | C-types, regolith fines       | Uses true waste, high Isp, targeted     | Nozzle erosion, CH₄ sourcing           |
| Water electrolysis + H₂/O₂| H₂ + O₂                     | ~450–500      | Phobos/NEA water              | Simple, abundant source                 | Low Isp, O₂ handling/compression       |
| Metal-oxygen              | Metal vapor + O₂            | 2 000–3 000   | Fe/Ni silicates               | Very high Isp, uses abundant metals     | High temp, complex reactor             |
| CO₂ thermal / Sabatier    | CO + O₂ or CH₄ + O₂         | 2 500–3 500   | Mars regolith CO₂             | In-situ on Mars, closes loop            | Energy intensive, catalyst issues      |
| Momentum-exchange tether  | No propellant               | N/A           | Tether mass (CNT)             | Zero consumable                         | Tether deployment & maintenance risk   |

## Scaling laws & bottlenecks

- **Early phase** (1–1 000 t/year): dominated by H₂O electrolysis + Uranus Ejector (waste-limited)  
- **Mid-phase** (1 000–100 000 t/year): metal-oxygen or CO₂ cycles become dominant as Fe/Ni/silicates become abundant  
- **Mature phase** (>10⁶ t/year): momentum-exchange tethers + beamed power reduce consumable needs to near zero  

Biggest early bottleneck: **CH₄ sourcing** for Uranus Ejector (C-types only ~10% of NEAs).  
Solution path: Sabatier reactors using CO₂ + H₂ → CH₄ + H₂O (recycles H₂O).

## Open questions

- Minimum CH₄ fraction needed for stable 10 km/s ejection  
- Energy cost of Sabatier vs direct CH₄ mining  
- When does tether-based propulsion become net-positive?  
- Safe exhaust vectoring rules to avoid Kessler syndrome  

This is still back-of-the-envelope.  
The economy only closes when waste = propellant closes at >90%.

Last updated: January 2026
