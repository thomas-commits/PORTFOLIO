import random

def mutate_antibody(antibody, mutation_rate=0.35):
    """
    Mutates an antibody by adjusting feature values slightly.
    """
    for key in antibody.keys():
        if random.random() < mutation_rate:
            antibody[key] += random.gauss(0, 0.1)  # Small random mutation
            antibody[key] = max(0, min(1, antibody[key]))  # Keep values in [0,1]
    return antibody