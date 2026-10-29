# Water Delivery Gear Ratio [WORKING]

How much mass has to be moved or mined to put 1 kg of water at a destination in cislunar space. This is the number that decides where off-Earth water starts to beat water launched from Earth, and the same reasoning applies to asteroid water once its delta-v to the customer is known.

## Model

One ideal expendable chemical stage per leg (Tsiolkovsky), stage dry mass 10% of the propellant it carries, Isp 450 s (H2/O2).

- **Earth source:** water and propellant start in LEO. The Earth-to-LEO launch is not counted, so these figures are "kg already in LEO per kg delivered".
- **Lunar source:** water is mined on the surface and the propellant is made from that water by electrolysis, so every kg of propellant costs about 1 kg of mined water.

Delta-v values: Wikipedia, *Delta-v budget*, table "Earth-Moon space, high thrust". Returns to LEO assume aerobraking.

| Destination | Earth source: kg in LEO per kg | Lunar source: kg mined per kg |
|---|---|---|
| LEO | 1.00 | 1.94 |
| GEO | 3.20 | 2.67 |
| EML-1 | 2.72 | 1.83 |
| Low lunar orbit | 2.94 | 1.56 |

Beyond LEO, lunar water needs 1.56 to 2.67 kg mined per kg delivered, while Earth water needs 2.72 to 3.20 kg already in LEO, before counting the 9.3 to 10 km/s ascent each of those LEO kilograms has already paid for.

## Limits

Screening model only: no boil-off, no reusable stages, no mining or processing equipment mass, no cost. A reusable tanker makes the off-Earth case better than shown here.

## Source code

Python and an in-browser calculator, Apache-2.0: [SpaceOceanCorp/space-water-logistics](https://github.com/SpaceOceanCorp/space-water-logistics) (`models/water_delivery_gear_ratio.py`). Change the delta-v table to an asteroid's numbers to get the same ratios for asteroid water.
