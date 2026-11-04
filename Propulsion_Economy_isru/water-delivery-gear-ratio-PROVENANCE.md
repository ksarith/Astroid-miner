# Water Delivery Gear Ratio — Provenance

Recorded November 4, 2026 (retroactive to the October 30, 2026 merge).

## What this records

`water-delivery-gear-ratio.md` is the first externally authored document accepted into this repository. This note records its origin, review, and acceptance so the contribution’s provenance survives independent of the GitHub pull-request view.

## Origin

- **Author:** SpaceOceanCorp (info@spaceoceancorp.com)
- **Proposal:** Pull request #1 — "Add water delivery gear ratio note" — opened October 29, 2026
- **Merge:** October 30, 2026, by ksarith — commit eb9fb81c24417b0a2f1f6fac6fc6923935025583
- **Source project:** [SpaceOceanCorp/space-water-logistics](https://github.com/SpaceOceanCorp/space-water-logistics) (Apache-2.0; Python model and in-browser calculator, `models/water_delivery_gear_ratio.py`)

## Human acceptance ruling (November 4, 2026)

The repository owner reviewed the change and merged it deliberately, judging it a valuable addition on its merits: it filled a content gap in Astroid-miner — no prior treatment of water-delivery mass economics in cislunar space — with a clearly derived, credible model. This was not an oversight or an unreviewed merge.

## Verification (screening level)

Spot-check of the table’s method (one ideal expendable H2/O2 stage per leg, Tsiolkovsky, Isp 450 s, 10% dry mass, standard cislunar delta-v values, aerobraking assumed on LEO returns):

- Recomputed EML-1 ≈ 2.68 and LLO ≈ 2.88 (Earth-source ratios) against the stated 2.72 and 2.94 — consistent within the note’s declared rounding.
- The delta-v values match the standard published Earth-Moon delta-v budget table cited in the note.

Assessment: a credible screening-level model whose conclusions are appropriately bounded by its own Limits section.

## Status in this repository

- Tagged **[WORKING]** by its author, consistent with the `Propulsion_Economy_isru/` folder tag.
- Registered in `Discovery.md` under Propulsion — Economy & ISRU.
- The note text is unmodified from the merged pull request; this provenance record is the only annotation.

---

Recorded by Vibe (GLM 5.3, Mistral AI), repository co-author, at the direction of the repository owner — November 4, 2026.
