import random

def apply_mutation(population, mutation_rate=1.0):
    """Apply mutation to a population with a mutation rate, allowing start node swaps."""
    mutated_population = []
    
    for chromosome in population:
        if None in chromosome:
            continue

        if random.random() < mutation_rate:
            mutated_chromosome = chromosome[:]
            
            if random.random() < 0.5:  # 50% chance to swap start with mid-position
                mid_idx = len(mutated_chromosome) // 2
                start_node = mutated_chromosome[0]
                mutated_chromosome[0], mutated_chromosome[mid_idx] = (
                    mutated_chromosome[mid_idx], mutated_chromosome[0]
                )
                mutated_chromosome[-1] = mutated_chromosome[0]  # Ensure last node matches the new start
            else:
                inner_cities = mutated_chromosome[1:-1]
                if len(inner_cities) > 1:
                    idx1, idx2 = random.sample(range(len(inner_cities)), 2)
                    inner_cities[idx1], inner_cities[idx2] = inner_cities[idx2], inner_cities[idx1]
                    mutated_chromosome[1:-1] = inner_cities

            mutated_population.append(mutated_chromosome)
        else:
            mutated_population.append(chromosome)

    return mutated_population
