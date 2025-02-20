import random
def uniform_crossover(parent1, parent2):
    """
    Uniform crossover: Each gene is randomly inherited from one of the parents.
    """
    offspring1 = [random.choice([g1, g2]) for g1, g2 in zip(parent1, parent2)]
    offspring2 = [random.choice([g1, g2]) for g1, g2 in zip(parent1, parent2)]
    
    return offspring1, offspring2
