import matplotlib.pyplot as plt

def plot_convergence(best_fitness_history, population_size, generations):
    """
    Plots the convergence of the genetic algorithm's fitness over generations.

    Parameters:
    - best_fitness_history (list): Best fitness values at each generation.
    - population_size (int): The population size used in the GA run.
    - generations (int): Total number of generations.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(range(len(best_fitness_history)), best_fitness_history, marker='o', linestyle='-', color='b', label="Best Fitness")

    plt.title(f'GA Convergence for Population Size {population_size}')
    plt.xlabel('Generation')
    plt.ylabel('Best Fitness')
    plt.legend()
    plt.grid(True)

    plt.show()
