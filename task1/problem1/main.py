from read_and_debug.read_and_debug_aggregator import read_and_debug
from parameter_arrays.parameter_arrays_aggregator import get_parameters
from genetic_algorithm.genetic_algorithm_aggregator import initialize_genetic_algorithm
from results.results_aggregator import plot_results
if __name__ == "__main__":
    params = get_parameters()  # Get parameters

    population_sizes = params["population_sizes"]  # Unpack population_sizes
    generation_values = params["generation_values"]  # Unpack generation_values

    dimension, coordinates, edge_weight_type = read_and_debug()  # Read dataset

    # Run the GA with tournament selection and capture the results
    evaluated_population, best_fitness_history_all_sizes, generations = initialize_genetic_algorithm(coordinates, population_sizes, generation_values, tournament_size=100, stagnation_limit=100)

    # Now you can print best_fitness_history_all_sizes:
    print("Best Fitness History for All Population Sizes:")
    for size, best_fitness_history in best_fitness_history_all_sizes.items():
        print(f"Population Size {size}: {best_fitness_history}")
    plot_results(best_fitness_history, generations)