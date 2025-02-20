import copy

def clone_antibodies(antibodies, scores, clone_factor=2):
    """
    Kloner antistoffer proporsjonalt med deres score.
    
    :param antibodies: Liste av antistoffer.
    :param scores: Liste med affinitetsscores for hvert antistoff.
    :param clone_factor: Hvor mange ganger hvert antistoff skal klones basert på score.
    :return: Liste av klonede antistoffer.
    """
    cloned_population = []
    
    for antibody, score in zip(antibodies, scores):
        num_clones = int(clone_factor * score)  # Flere kloner for bedre antistoffer
        cloned_population.extend([copy.deepcopy(antibody) for _ in range(num_clones)])
    
    return cloned_population