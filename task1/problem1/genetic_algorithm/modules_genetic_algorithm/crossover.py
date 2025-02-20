import random
def order_one_crossover(parent1, parent2):
    size = len(parent1)
    
    # Step 1: Choose random crossover points
    point1, point2 = sorted(random.sample(range(size), 2))
    
    # Step 2: Create offspring by copying the segment from parent1 and parent2
    offspring1 = [None] * size
    offspring2 = [None] * size

    # Copy the selected segment from parent1 to offspring1 and from parent2 to offspring2
    offspring1[point1:point2] = parent1[point1:point2]
    offspring2[point1:point2] = parent2[point1:point2]

    # Step 3: Fill in the remaining positions with non-repeating genes
    fill1 = [gene for gene in parent2 if gene not in offspring1]  # Remaining genes from parent2 for offspring1
    fill2 = [gene for gene in parent1 if gene not in offspring2]  # Remaining genes from parent1 for offspring2

    # Ensure all fill lists are populated correctly
    for i in range(size):
        if offspring1[i] is None:
            offspring1[i] = fill1.pop(0) if fill1 else None
        if offspring2[i] is None:
            offspring2[i] = fill2.pop(0) if fill2 else None

     # Ensure the last city is the same as the starting city
        if offspring1[-1] != offspring1[0]:
            offspring1[-1] = offspring1[0]
        if offspring2[-1] != offspring2[0]:
            offspring2[-1] = offspring2[0]            
            # Ensure the last city is the same as the starting city

    return offspring1, offspring2
