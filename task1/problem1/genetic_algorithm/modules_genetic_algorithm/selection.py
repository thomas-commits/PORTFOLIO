import random

def tournament_selection(evaluated_population, num_parents, tournament_size):
    """
    Selects the best individuals using tournament selection.
    Ensures that selected parents have the best fitness (lowest distance).
    """
    selected_parents = []
    
    # Sort population by fitness (ascending order since lower is better)
    sorted_population = sorted(evaluated_population, key=lambda x: x[1])

    while len(selected_parents) < num_parents:
        # Randomly sample `tournament_size` individuals
        tournament_contestants = random.sample(sorted_population, tournament_size)
        
        # Select the best (lowest distance) from the tournament
        best_individual = min(tournament_contestants, key=lambda x: x[1])  

        # Add to selected parents
        selected_parents.append(best_individual)

    return selected_parents  # Returns a list of (chromosome, fitness)
