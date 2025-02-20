import random
from collections import Counter

def create_initial_population(size, spam_antigens, ham_antigens):
    """
    Creates an initial population of antibodies, biased by word frequencies in spam and ham datasets.
    
    :param size: Number of antibodies in the population.
    :param spam_antigens: List of spam email word frequency dictionaries.
    :param ham_antigens: List of ham email word frequency dictionaries.
    :return: List of initialized antibodies.
    """
    # Extract all unique words from spam and ham
    feature_space = set(word for antigen in spam_antigens + ham_antigens for word in antigen)

    # Count word frequencies in spam vs ham datasets
    spam_word_counts = Counter(word for antigen in spam_antigens for word in antigen)
    ham_word_counts = Counter(word for antigen in ham_antigens for word in antigen)

    # Create antibodies with values based on word occurrences
    population = []
    for _ in range(size):
        antibody = {}
        for word in feature_space:
            spam_freq = spam_word_counts[word] + 1  # Avoid zero division
            ham_freq = ham_word_counts[word] + 1

            # Set initial weight with a slight spam/ham bias
            antibody[word] = random.uniform(0, 1) * (spam_freq / ham_freq)

        population.append(antibody)
    
    return population