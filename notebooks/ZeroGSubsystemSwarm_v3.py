import numpy as np
from dataclasses import dataclass
from typing import Dict, List, Any

# =============================================
# Constraint Graph for Astroid-miner Zero-G Replication
# Modular subsystems with explicit dependencies
# =============================================

@dataclass
class Asteroid:
    name: str
    composition: Dict[str, float]
    cohesion_kpa: float = 15.0

class Subsystem:
    def __init__(self, name: str, mass_fraction: float):
        self.name = name
        self.mass_fraction = mass_fraction
        self.state = {}  # e.g. dust, temperature

    def capacity(self, swarm_mass: float, params: Dict, global_state: Dict) -> float:
        """Maximum output this subsystem can provide this cycle."""
        raise NotImplementedError

    def demand(self, flow: float, params: Dict) -> float:
        """Resources (power, mass, etc.) demanded to achieve target flow."""
        return 0.0

class PowerSubsystem(Subsystem):
    def capacity(self, swarm_mass: float, params: Dict, global_state: Dict) -> float:
        mass = swarm_mass * self.mass_fraction
        solar = mass * params['panel_specific_power_kw_per_kg'] * (1.0 / params['au_distance']**2)
        return solar

class AnchorSubsystem(Subsystem):
    def capacity(self, swarm_mass: float, params: Dict, global_state: Dict) -> float:
        # Max force before slip
        mass = swarm_mass * self.mass_fraction
        return mass * params['anchoring_force_n_per_kg']

class MiningSubsystem(Subsystem):
    def capacity(self, swarm_mass: float, params: Dict, global_state: Dict) -> float:
        anchor_limit = global_state.get('anchor_capacity', 1e6)
        throttle = min(1.0, anchor_limit / max(global_state.get('cohesion_force', 1), 1e-6))
        mass = swarm_mass * self.mass_fraction
        return mass * params['dig_rate_kg_per_kg'] * throttle

class RefiningSubsystem(Subsystem):
    def capacity(self, swarm_mass: float, params: Dict, global_state: Dict) -> float:
        mass = swarm_mass * self.mass_fraction
        spin_tax = mass * params.get('spin_power_tax_kw_per_kg', 0.005)
        available_power = max(0, global_state.get('power_available', 0) - spin_tax)
        return min(mass * params['refining_rate'], available_power * params['kg_per_kwh'])

class FabricationSubsystem(Subsystem):
    def capacity(self, swarm_mass: float, params: Dict, global_state: Dict) -> float:
        mass = swarm_mass * self.mass_fraction
        base = mass * params['fab_rate']
        yield_bonus = 1.15 if params.get('micro_g_slurry', True) else 1.0
        return base * params['base_fab_yield'] * yield_bonus

class ConstraintSolver:
    def __init__(self, subsystems: List[Subsystem], params: Dict):
        self.subsystems = {s.name: s for s in subsystems}
        self.params = params

    def solve_cycle(self, swarm_mass: float, asteroid: Asteroid, collection_method: str = "enclosed"):
        global_state = {}
        
        # Power
        global_state['power_available'] = self.subsystems['Power'].capacity(swarm_mass, self.params, global_state)
        
        # Anchor
        global_state['anchor_capacity'] = self.subsystems['Anchor'].capacity(swarm_mass, self.params, global_state)
        global_state['cohesion_force'] = asteroid.cohesion_kpa * self.params['tool_area_m2'] * 1000
        
        # Mining
        mined = self.subsystems['Mining'].capacity(swarm_mass, self.params, global_state)
        
        # Refining
        refined_raw = self.subsystems['Refining'].capacity(swarm_mass, self.params, global_state)
        processed = min(mined, refined_raw)
        
        refined_metal = processed * asteroid.composition.get('metal', 0.15)
        
        # Fabrication
        fab = self.subsystems['Fabrication'].capacity(swarm_mass, self.params, global_state)
        
        # Simple salvage placeholder (expand later)
        fabricated = min(fab, refined_metal * 1.2)  # rough
        
        return {
            'mined': mined,
            'processed': processed,
            'fabricated': fabricated,
            'power_available': global_state['power_available'],
            'bottleneck': max(['Power', 'Anchor', 'Mining', 'Refining', 'Fabrication'], 
                            key=lambda n: -self.subsystems[n].capacity(swarm_mass, self.params, global_state) if n in self.subsystems else 0)
        }

# Example usage
params = {
    'au_distance': 1.3,
    'panel_specific_power_kw_per_kg': 0.08,
    'anchoring_force_n_per_kg': 15.0,
    'tool_area_m2': 0.05,
    'dig_rate_kg_per_kg': 15.0,
    'refining_rate': 12.0,
    'kg_per_kwh': 2.5,
    'fab_rate': 8.0,
    'base_fab_yield': 0.65,
    'spin_power_tax_kw_per_kg': 0.005,
    'micro_g_slurry': True,
}

fractions = {
    'Power': 0.28, 'Anchor': 0.10, 'Mining': 0.20,
    'Refining': 0.18, 'Fabrication': 0.15, 'Other': 0.09
}

subsystems = [
    PowerSubsystem('Power', fractions['Power']),
    AnchorSubsystem('Anchor', fractions['Anchor']),
    MiningSubsystem('Mining', fractions['Mining']),
    RefiningSubsystem('Refining', fractions['Refining']),
    FabricationSubsystem('Fabrication', fractions['Fabrication'])
]

solver = ConstraintSolver(subsystems, params)
asteroid = Asteroid("C-type", {"water":0.12, "metal":0.18, "silicates":0.70})

result = solver.solve_cycle(8000.0, asteroid)
print(result)
