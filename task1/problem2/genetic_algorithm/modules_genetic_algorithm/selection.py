import random

def tournament_selection(population, fitness_values, tournament_size=3):
    """
    Tournament selection: Pick 'tournament_size' random individuals and select the best one.
    """
    selected = random.sample(list(zip(population, fitness_values)), tournament_size)
    best_individual = max(selected, key=lambda x: x[1])[0]
    return best_individual
