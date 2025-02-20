import random
def adaptive_mutation(chromosome, fitness, best_fitness, generation, max_generations):
    """
    Reduce mutation rate for high-fitness individuals and as generations progress.
    """
    base_mutation = 1.0  # Base mutation rate
    fitness_factor = (best_fitness - fitness) / best_fitness if best_fitness > 0 else 1
    generation_factor = (1000 - generation) / 1000  # Reduce over time

    mutation_rate = base_mutation * fitness_factor * generation_factor  # Adjusted mutation rate
        
    mutated_chromosome = chromosome[:]
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            mutated_chromosome[i] = 1 - mutated_chromosome[i]  # Flip bit
    
    return mutated_chromosome
