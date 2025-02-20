from results.modules_results.solution import print_final_populations
from results.modules_results.plot import plot_convergence  # Import the plotting function


def plot_results(best_fitness_over_time, generations):
    plot_convergence(best_fitness_over_time, generations, generations)
