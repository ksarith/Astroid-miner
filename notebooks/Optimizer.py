def optimize_mass_allocation(solver, current_mass: float, asteroid: Asteroid, cycle: int, epsilon=0.01) -> Dict[str, float]:
    baseline = solver.solve_cycle(current_mass, asteroid, cycle)
    baseline_growth = baseline['net_growth']
    
    gradients = {}
    original_fractions = {name: sub.mass_fraction for name, sub in solver.subsystems.items()}
    
    for target in solver.subsystems.keys():
        perturbed = original_fractions.copy()
        perturbed[target] += epsilon
        total_others = sum(v for k, v in perturbed.items() if k != target)
        scale = (1.0 - perturbed[target]) / (total_others + 1e-9)
        for k in perturbed:
            if k != target:
                perturbed[k] *= scale
        
        # Apply & evaluate
        for name, frac in perturbed.items():
            solver.subsystems[name].mass_fraction = frac
        perturbed_result = solver.solve_cycle(current_mass, asteroid, cycle)
        gradients[target] = (perturbed_result['net_growth'] - baseline_growth) / epsilon
    
    # Restore
    for name, frac in original_fractions.items():
        solver.subsystems[name].mass_fraction = frac
    
    return gradients
