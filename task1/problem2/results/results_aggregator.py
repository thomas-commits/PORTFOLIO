from results.modules_results.plot import plot_convergence  # Import the plotting function


def plot_results(best_fitness_history, generations):
    plot_convergence(best_fitness_history, generations)
