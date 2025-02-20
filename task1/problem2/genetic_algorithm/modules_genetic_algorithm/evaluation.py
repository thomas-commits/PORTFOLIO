def calculate_fitness(chromosome, profit, weight, weight_limit):
    """Calculate the fitness of an individual chromosome."""
    total_profit = 0
    total_weight = 0
    
    for i in range(len(chromosome)):
        if chromosome[i] == 1:  # If the item is selected in the solution
            total_profit += profit[i]  # Add the profit of the item
            total_weight += weight[i]  # Add the weight of the item

    # If total weight exceeds the limit, return 0
    if total_weight > weight_limit:
        return 0  # Penalize the solution if it exceeds the weight limit

    return total_profit


def evaluate_population(population, profit, weight, weight_limit):
    """Evaluate the fitness of each chromosome in the population."""
    fitness_values = []
    for chromosome in population:
        fitness = calculate_fitness(chromosome, profit, weight, weight_limit)
        fitness_values.append(fitness)
    return fitness_values
