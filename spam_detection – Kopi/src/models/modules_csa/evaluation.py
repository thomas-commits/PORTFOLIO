import numpy as np

def evaluate_antibody(antibody, antigen):
    """
    Beregner likheten mellom et antistoff og et antigen.
    
    :param antibody: Dictionary med trekk og vektverdier.
    :param antigen: Dictionary med trekk og deres observerte verdier.
    :return: En score mellom 0 og 1 som måler affiniteten.
    """
    common_keys = set(antibody.keys()) & set(antigen.keys())
    if not common_keys:
        return 0  # Ingen overlapp mellom antistoff og antigen
    
    antibody_vector = np.array([antibody[key] for key in common_keys])
    antigen_vector = np.array([antigen[key] for key in common_keys])
    
    # Kosinuslikhet mellom antistoff og antigen
    similarity = np.dot(antibody_vector, antigen_vector) / (np.linalg.norm(antibody_vector) * np.linalg.norm(antigen_vector))
    norm_antibody = np.linalg.norm(antibody_vector)
    norm_antigen = np.linalg.norm(antigen_vector)
    if norm_antibody == 0 or norm_antigen == 0:
        return 0  # Unngå divisjonsfeil

    
    return similarity