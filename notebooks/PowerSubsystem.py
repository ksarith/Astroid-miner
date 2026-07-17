class PowerSubsystem(Subsystem):
    def __init__(self, mass_fraction: float, hts_enabled: bool = False, dormant_spares_fraction: float = 0.15):
        super().__init__('Power', mass_fraction)
        self.hts_enabled = hts_enabled
        self.dormant_spares_fraction = dormant_spares_fraction  # From Fault-Tolerant-Power-Control.md

    def capacity(self, swarm_mass: float, params: Dict, cycle: int = 0) -> float:
        base_specific = params['panel_specific_power_kw_per_kg']
        
        # Degradation (radiation, thermal cycling, dust)
        degradation = (1.0 - params.get('power_degradation_per_cycle', 0.025)) ** cycle
        effective_specific = base_specific * degradation
        
        # HTS mass penalty (encapsulation, shielding)
        if self.hts_enabled:
            effective_specific *= params.get('hts_mass_penalty_factor', 0.78)  # \~22% penalty
        
        power_mass = swarm_mass * self.mass_fraction * (1 - self.dormant_spares_fraction)
        gross_power = power_mass * effective_specific * (1.0 / params['au_distance']**2)
        
        # Transmission efficiency
        eta_trans = params.get('hts_transmission_efficiency', 0.98) if self.hts_enabled else params.get('baseline_transmission_efficiency', 0.85)
        
        return gross_power * eta_trans
