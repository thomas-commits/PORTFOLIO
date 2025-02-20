import random

def generate_chromosome(dimension):
    """
    Generate a random chromosome (bitstring) of a given dimension.
    Each bit is either 0 or 1, representing the presence or absence of an item.
    """
    chromosome = [random.choice([0, 1]) for _ in range(dimension)]
    return chromosome

def initialize_population(population_size, dimension):
    """
    Generate an initial population of chromosomes.
    """
    population = []
    for _ in range(population_size):
        chromosome = generate_chromosome(dimension)  # Generate a chromosome (bitstring)
        population.append(chromosome)
    return population
