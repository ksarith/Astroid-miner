import numpy as np
from typing import Dict, Any

class Asteroid:
    def __init__(self, name: str, composition: Dict[str, float], cohesion_kpa: float = 15.0):
        total = sum(composition.values())
        self.name = name
        self.composition = {k: v / total for k, v in composition.items()}
        self.cohesion_kpa = cohesion_kpa

class ConstraintSolver:
    def __init__(self, params: Dict[str, Any]):
        self.params = params

    def solve_cycle(self, swarm_mass: float, asteroid: Asteroid) -> Dict[str, Any]:
        # (Power, spin tax, anchoring throttle, refining, etc. as before)
        # ... [full power/anchor/mining/refining logic from previous versions]

        # Silicate Pathway (new)
        raw_silicates = processed_raw_kg * asteroid.composition.get('silicates', 0.70)
        sil_products = self.process_silicates(raw_silicates, swarm_mass)

        # SiC Wear Reduction
        sic_ratio = sil_products['sic_ceramics'] / (processed_raw_kg + 1e-6)
        mitigated_failure = self.params.get('base_failure_rate', 0.06) * np.exp(-1.5 * sic_ratio)

        # Basalt Fiber Substitution
        fiber_ratio = sil_products['glass_fibers'] / (raw_metals + 1e-6)
        substitution = min(self.params.get('max_basalt_substitution', 0.35), fiber_ratio)
        metal_discount = 1.0 - substitution

        # Fabrication with discount
        total_structural = raw_metals / (metal_discount + 1e-6)
        fabricated = min(fab_capacity, total_structural) * self.params['base_fab_yield']

        return {
            'fabricated': fabricated,
            'net_growth': fabricated - (swarm_mass * mitigated_failure),
            'silicate_products': sil_products,
            'effective_failure_rate': mitigated_failure,
            'basalt_substitution': substitution,
            'active_bottleneck': ... 
        }

    def process_silicates(self, input_kg: float, swarm_mass: float) -> Dict[str, float]:
        # From the pasted code
        processed = min(input_kg, swarm_mass * self.params.get('silicate_processing_rate', 10.0) * 0.09)  # fraction
        return {
            'sic_ceramics': processed * 0.30,
            'glass_fibers': processed * 0.45,
            'sintered_regolith': processed * 0.20,
            'losses': processed * 0.05
        }
