import random
from genetic_algorithm.modules_genetic_algorithm.initialization import generate_chromosome
from genetic_algorithm.modules_genetic_algorithm.evaluation import compute_distance_matrix, evaluate_population
from genetic_algorithm.modules_genetic_algorithm.selection import tournament_selection
from genetic_algorithm.modules_genetic_algorithm.crossover import order_one_crossover
from genetic_algorithm.modules_genetic_algorithm.mutation import apply_mutation
from genetic_algorithm.modules_genetic_algorithm.termination import check_for_bugs  # Import termination check


def initialize_genetic_algorithm(coordinates, population_sizes, generation_values, tournament_size=100, stagnation_limit=100):
    dimension = len(coordinates)
    distance_matrix = compute_distance_matrix(coordinates)

    best_fitness_history_all_sizes = {}

    for size in population_sizes:
        population = [generate_chromosome(dimension) for _ in range(size)]
        evaluated_population = evaluate_population(population, distance_matrix)

        print(f"\nStarting Genetic Algorithm with Population Size {size}")

        best_fitness_history = []

        for generations in generation_values:
            print(f"\nRunning for up to {generations} generations...")

            for generation in range(1, generations + 1):
                print(f"\nGeneration {generation}:")

                #if check_for_bugs(evaluated_population, generation, best_fitness_history, stagnation_limit):
                 #   print("\nStopping early due to detected issue.")
                  #  return evaluated_population, best_fitness_history

                # Evaluate and track best fitness
                best_chromosome, best_fitness = min(evaluated_population, key=lambda x: x[1])
                best_fitness_history.append(best_fitness)

                print(f"Best Fitness in Generation {generation}: {best_fitness}")

                # Selection: Keep the best half of the population
                num_parents = size // 2
                actual_tournament_size = min(tournament_size, len(evaluated_population))

                parents = tournament_selection(evaluated_population, num_parents, tournament_size=3)
                parent_chromosomes = [p[0] for p in parents]

                # Generate offspring to replace the other half
                offspring_population = []
                while len(offspring_population) < (size - num_parents):
                    parent1, parent2 = random.sample(parent_chromosomes, 2)
                    offspring1, offspring2 = order_one_crossover(parent1, parent2)
                    offspring_population.extend([offspring1, offspring2])

                offspring_population = offspring_population[:(size - num_parents)]

                # Apply mutation to offspring
                mutated_offspring_population = apply_mutation(offspring_population)

                # New population: Keep parents + offspring
                new_population = parent_chromosomes + mutated_offspring_population

                # Ensure the best solution is carried forward (elitism)
                evaluated_new_population = evaluate_population(new_population, distance_matrix)
                current_best = min(evaluated_new_population, key=lambda x: x[1])

                if current_best[1] > best_fitness:
                    evaluated_new_population[-1] = (best_chromosome, best_fitness)

                evaluated_population = evaluated_new_population

            best_fitness_history_all_sizes[size] = best_fitness_history

    return evaluated_population, best_fitness_history_all_sizes, generations