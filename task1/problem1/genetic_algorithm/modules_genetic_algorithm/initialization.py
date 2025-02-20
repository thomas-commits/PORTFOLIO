import random

def generate_chromosome(dimension):
    """Generate a random chromosome (path through cities), starting and ending at the same random node."""
    start_node = random.randint(0, dimension - 1)  # Choose a random start node
    chromosome = list(range(dimension))  # Create a list of all cities
    chromosome.remove(start_node)  # Remove the start node from the list
    random.shuffle(chromosome)  # Randomize the order of remaining cities
    chromosome.insert(0, start_node)  # Set the start node at the beginning
    chromosome.append(start_node)  # Ensure the path returns to the start node
    return chromosome 


