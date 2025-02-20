def check_for_bugs(evaluated_population, generation, best_fitness_history, stagnation_limit=100):
    """
    Stops if best fitness has not improved for `stagnation_limit` generations.
    """
    fitness_values = [fitness for _, fitness in evaluated_population]
    best_fitness = min(fitness_values)

    # If fitness hasn't improved in `stagnation_limit` generations, stop
    if len(best_fitness_history) >= stagnation_limit and all(
        best_fitness >= previous_fitness for previous_fitness in best_fitness_history[-stagnation_limit:]
    ):
        print(f"Stopping: No improvement in {stagnation_limit} generations.")
        return True

    best_fitness_history.append(best_fitness)
    return False
