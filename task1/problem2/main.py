from read_and_debug.read_and_debug_aggregator import read_and_debug
from genetic_algorithm.genetic_algorithm_aggregator import genetic_algorithm
from results.results_aggregator import plot_results
if __name__ == "__main__":
    # Read and extract values using the updated read_and_debug function
    dimension, weight_limit, profit, weight = read_and_debug()  # Extract the values

    # Now that we have the dimension, weight_limit, profit, and weight, pass them to the genetic algorithm
    if dimension and weight_limit and profit and weight:  # Check if the values are valid
        best_fitness_over_time, generations = genetic_algorithm(dimension, weight_limit, profit, weight)
    else:
        print("Error: Invalid data received. Cannot run the genetic algorithm.")

    plot_results(best_fitness_over_time, generations)    

