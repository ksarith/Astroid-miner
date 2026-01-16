# Rogue Unit Protocol

How the Leviathan Swarm detects, isolates, contains, and (if necessary) neutralizes rogue units.

## Why we need a dedicated protocol

A single rogue module can:
- Misdirect thousands of tonnes of H₂O, CO₂ or CH₄ per year
- Trigger Kessler-like debris cascades
- Corrupt swarm coordination (10⁸ bits/s laser backbone)
- Cost $15M+ in lost hardware and months of recovery
- Put the entire replication loop at risk

The protocol exists to keep rogue probability <0.01% at scale and ensure that when it happens (and it will), the damage is contained to one or a few units.

## Detection triggers

| Trigger type               | Typical cause                          | Detection method                          | Threshold / sensitivity          |
|----------------------------|----------------------------------------|-------------------------------------------|----------------------------------|
| Trajectory anomaly         | Bit flip, thruster fault               | LIDAR + orbital ephemeris comparison      | >0.1° deviation                  |
| Comms silence / gibberish  | Radiation, software fault              | Packet loss or invalid checksum           | >1% loss over 60 s               |
| AI divergence              | Cosmic ray, adversarial input          | Decentralized consensus mismatch          | >0.01% deviation from swarm      |
| Unauthorized maneuver      | Hostile rewrite, malware               | Behavioral anomaly scoring                | Any non-protocol Δv burn         |
| Ejector misfire            | Mechanical or propellant fault         | Thrust vector telemetry                   | >5% off-nominal burn             |

All triggers feed into the swarm’s hierarchical consensus (99.99% agreement required to declare rogue status).

## Protocol stages

1. **Alert (0–60 seconds)**  
   - Swarm AI flags anomaly  
   - Nearby units (10–50) begin passive tracking  
   - No action yet — just heightened monitoring

2. **Isolation & Challenge (60 s – 5 min)**  
   - Quantum-encrypted RTB signal broadcast (512-bit QKD, 10 Gbps)  
   - Rogue given 30 s to acknowledge and comply  
   - If no response → marked as rogue, comms channels restricted

3. **Non-destructive response (preferred path)**  
   a. **Return-to-Base (RTB)**  
      - Uranus Probe(s) launched from nearest sentinel micros  
      - 10 000 m/s intercept (10 s at 100 km, 2 h at 1 000 km)  
      - CNT tether latch (99% hit rate at 1 km)  
      - Dock → override AI → return to hub (98% success at close range)  

   b. **Core Swap**  
      - Probe carries spare AI core (10 kg)  
      - Docks, swaps core (10 min via micro-arms)  
      - Rogue resumes normal operation (99.9% uptime preserved)  
      - Old core returned to hub for forensic analysis  

   c. **Redirection / Containment**  
      - Single probe: tether + 10 000 m/s nudge (100–1 000 km off-orbit)  
      - Multi-probe: 5-probe CNT net (5 km²), collective drag to safe zone (5 000 m/s, 1 day)  

4. **Last-resort neutralization (only if collision imminent)**  
   - Probe overloads ejector (100 kg CH₄, 20 000 m/s ram)  
   - Fragments directed away from swarm (1% Kessler odds target)  
   - Debris tracked by sentinel micros for later cleanup  

## Key technologies enabling the protocol

- **Uranus Probe** (10 kg, 10 000 m/s, 1 km tether, quantum comms)  
- **QKD + blockchain consensus** (tamper-proof RTB signal, 10¹² bit/s entropy)  
- **Thermite self-destruct** (probe core melts in 10 s if tampered)  
- **Sentinel escort** (10 micros per probe, 10 000 m/s defensive nudge)  
- **Spare core inventory** (10 kg hot-swap units carried by probes)

## Scaling considerations

| Swarm size         | Estimated rogue rate | Probes needed (target 98% coverage) | Notes                              |
|--------------------|----------------------|-------------------------------------|------------------------------------|
| 10⁴ modules        | ~0.1–0.5%            | 10–50                               | Early phase, mostly test failures  |
| 10⁶ modules        | ~0.01–0.1%           | 500–1 000                           | Transition to production swarm     |
| 10⁸–10⁹ modules    | <0.001%              | 5 000–10 000                        | Mature exponential phase           |

## Open questions

- Minimum number of probes per million modules for 98% intercept probability
- Maximum safe tether length (1 km baseline — 2 km worth the mass penalty?)
- Overload ram debris profile (acceptable fragment size / velocity?)
- How to handle “partially rogue” units (e.g., thruster stuck on, but AI still responsive)

This protocol is still conceptual.  
It will almost certainly change after the first real rogue incident.

Last updated: January 2026
