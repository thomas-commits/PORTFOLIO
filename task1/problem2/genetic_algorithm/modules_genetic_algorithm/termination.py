def termination(generation, max_generations, fitness_values, target_fitness=32000, stagnation_threshold=50):
    """
    Determine whether the algorithm should stop based on various conditions:
    1. Maximum generations reached.
    2. Target fitness level reached.
    3. Stagnation for a certain number of generations.
    """
    # Check if the maximum number of generations has been reached
    if generation >= max_generations:
        print("Max generations reached.")
        return True
    
    # Check if the target fitness has been reached
    if max(fitness_values) >= target_fitness:
        print("Target fitness reached.")
        return True
    
    # Check for stagnation (if no improvement in fitness over a number of generations)
    # Stagnation is defined as having no improvement for a set number of generations
    stagnant_generations = 0
    for i in range(1, len(fitness_values)):
        if fitness_values[i] == fitness_values[i-1]:
            stagnant_generations += 1
        else:
            stagnant_generations = 0  # Reset if there's improvement
    
    if stagnant_generations >= stagnation_threshold:
        print(f"Algorithm stagnated for {stagnation_threshold} generations.")
        return True
    
    return False
