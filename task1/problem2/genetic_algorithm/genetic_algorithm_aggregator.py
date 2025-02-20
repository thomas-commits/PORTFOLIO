import random
from genetic_algorithm.modules_genetic_algorithm.initialization import initialize_population
from genetic_algorithm.modules_genetic_algorithm.evaluation import evaluate_population
from genetic_algorithm.modules_genetic_algorithm.selection import tournament_selection
from genetic_algorithm.modules_genetic_algorithm.crossover import uniform_crossover
from genetic_algorithm.modules_genetic_algorithm.mutation import adaptive_mutation
from genetic_algorithm.modules_genetic_algorithm.termination import termination

def track_best_fitness(fitness_values):
    """Returns the best fitness value from the current population."""
    return max(fitness_values)

def genetic_algorithm(dimension, weight_limit, profit, weight, population_size=1000, generations=1000, mutation_rate=0.01, crossover_rate=0.7, target_fitness=33000):
    """Run the genetic algorithm and track best fitness values for convergence plotting."""
    population = initialize_population(population_size, dimension)
    
    # List to store the best fitness for each generation
    best_fitness_over_time = []

    for generation in range(generations):
        # Evaluate fitness of the population
        fitness_values = evaluate_population(population, profit, weight, weight_limit)

        # Track best fitness
        best_fitness = track_best_fitness(fitness_values)
        best_fitness_over_time.append(best_fitness)

        # Sort the population based on fitness values (descending order)
        fitness_chromosomes = list(zip(fitness_values, population))
        fitness_chromosomes.sort(reverse=True, key=lambda x: x[0])

        # Print top individuals
        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")
        print(f"Top 10 Best Chromosomes (by fitness):")
        for i in range(min(10, len(fitness_chromosomes))):  
            print(f"Chromosome {i + 1}: Fitness = {fitness_chromosomes[i][0]} - {fitness_chromosomes[i][1]}")

        # Keep the best individuals (Elitism without direct elitism)
        num_elites = max(1, population_size // 10)  # Keep 10% of the best individuals
        elite_individuals = [ind for _, ind in fitness_chromosomes[:num_elites]]

        # Perform selection for new parents
        parents = []
        while len(parents) < population_size // 2:
            parents.append(tournament_selection(population, fitness_values))

        # Generate offspring
        offspring = []
        while len(offspring) < population_size // 2:
            parent1 = tournament_selection(population, fitness_values)
            parent2 = tournament_selection(population, fitness_values)

            if random.random() < crossover_rate:
                offspring1, offspring2 = uniform_crossover(parent1, parent2)
            else:
                offspring1, offspring2 = parent1[:], parent2[:]  # No crossover

            # Apply adaptive mutation
            offspring1 = adaptive_mutation(offspring1, best_fitness, generation, generations, 1000)
            offspring2 = adaptive_mutation(offspring2, best_fitness, generation, generations, 1000)

            offspring.extend([offspring1, offspring2])

        # Update population: Keep best individuals + new offspring
        population = elite_individuals + offspring[:population_size - len(elite_individuals)]

        # Check termination condition
        if termination(generation, generations, fitness_values, target_fitness):
            print("Termination condition met.")
            break

    return best_fitness_over_time, generation
