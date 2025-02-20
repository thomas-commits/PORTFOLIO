import matplotlib.pyplot as plt

def plot_convergence(best_fitness_history, generations):
    """
    Visualizes the convergence of fitness values over generations.

    Parameters:
    best_fitness_over_time (list): List containing the best fitness values at each generation.
    generations (int): The total number of generations to mark on the plot.
    """
    # Plot the fitness values
    plt.plot(range(len(best_fitness_history)), best_fitness_history, marker='o', linestyle='-', color='b')

    # Adding labels and title
    plt.title('Convergence of the Genetic Algorithm')
    plt.xlabel('Generation')
    plt.ylabel('Best Fitness')

    # Safely annotate if the list has the required number of generations
    for generation in range(1, generations + 1):  # We loop over all generations
        if generation - 1 < len(best_fitness_history):
            plt.annotate(f'Generation {generation}', 
                         xy=(generation - 1, best_fitness_history[generation - 1]), 
                         xytext=(generation, best_fitness_history[generation - 1] + 10),
                         arrowprops=dict(arrowstyle='->', color='r'), 
                         color='r')

    # Display the plot after the final generation
    plt.show()
