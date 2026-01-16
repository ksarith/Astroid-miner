# 01 – Guiding Principles & Recurring Clichés

This is not a mission statement or corporate values deck.  
It is simply a collection of mental anchors that have come up repeatedly while thinking through asteroid mining, self-replication, rogue mitigation, bootstrapping under extreme constraints, and the long path to multi-planetary industry.

They are kept short, sometimes deliberately blunt, because complex systems reward clarity over elegance.

## Core principles

1. **A little forethought can save a whole lot of heartache**  
   → Most catastrophic failures in space systems are foreseeable with basic scenario planning.  
   Spend time on Kessler syndrome, rogue unit protocols, reaction mass starvation, single-point failures, and legal/regulatory tripwires *before* hardware flies.

2. **War doesn’t determine who is right — war determines who is left**  
   → In space, survival trumps being philosophically correct.  
   Design for redundancy, graceful degradation, fault isolation, and worst-case energy/mass budgets — not for winning arguments about the One True Architecture.

3. **Truth is truth, no matter what**  
   → If a 1960s paper, a random forum post, a sci-fi novel, or an academic rival has a correct insight, use it.  
   Ego, source prestige, and aesthetic appeal are irrelevant. Reality doesn’t care who said it first.

4. **There is an exception to every rule, except this one**  
   → Every engineering heuristic, scaling law, and safety margin will eventually be broken by edge cases.  
   Build systems that can survive being wrong about their own assumptions (over-design reaction mass, over-provision compute, over-test autonomy).

5. **The only thing I can say with certainty is I know nothing**  
   → We are still in the pre-paradigmatic phase of asteroid mining.  
   Treat every number, every mass budget, every timeline, every ISRU efficiency as provisional and likely wrong.  
   Build the repo and the thinking to be wrong in public, quickly, and cheaply — so we can become less wrong faster.

## Operational attitudes derived from the above

- Start ugly and cheap — the first replicating loop does not need to be beautiful or profitable, only self-sustaining at gram → kilogram → tonne scale.
- Waste is propellant — every gram that is not product should ideally become reaction mass or radiation shielding.
- Redundancy > optimization in the bootstrap phase — optimization comes after the loop is closed.
- Assume everything will be stolen, spoofed, or irradiated — design accordingly (QKD, thermite self-destruct, radiation-hardened everything).
- Iterate in public — the fastest way to find the real bugs is to let smart strangers see your ugly first drafts.

These are not sacred.  
They are heuristics that have survived repeated stress-testing in thought experiments and back-of-the-envelope calculations.

If any of them stop being useful, discard them without sentiment.

Last updated: January 2026
