from src.models.modules_csa.encoding import encode_emails_as_antigens
from src.models.modules_csa.population_creation import create_initial_population
from src.models.modules_csa.evaluation import evaluate_antibody
from src.models.modules_csa.clone import clone_antibodies
from src.models.modules_csa.mutation import mutate_antibody
import random 
def initialize_antigens(spam_emails, easy_ham_emails):
    """
    Initializes antigen representations for spam and ham emails.

    :param spam_emails: List of spam emails.
    :param easy_ham_emails: List of ham emails.
    :return: Two lists with antigen representations.
    """
    spam_antigens = encode_emails_as_antigens(spam_emails)
    ham_antigens = encode_emails_as_antigens(easy_ham_emails)
    
    return spam_antigens, ham_antigens



def train(spam_antigens, ham_antigens, num_generations=10, population_size=50):
    """
    Train the CSA algorithm to detect spam and ham emails. 
    Uses both spam and ham antigens during evaluation.

    :param spam_antigens: List of spam antigens (encoded emails).
    :param ham_antigens: List of ham antigens (encoded emails).
    :param num_generations: Number of generations for CSA.
    :param population_size: Size of the population of antibodies.
    :return: Trained antibodies.
    """
    # Create the feature space from both spam and ham antigens
    feature_space = set(word for antigen in spam_antigens + ham_antigens for word in antigen)

    # Create the initial population of antibodies using both spam and ham
    population = create_initial_population(population_size, spam_antigens, ham_antigens)

    for generation in range(num_generations):
        print(f"Generation {generation+1}/{num_generations}")

        # Step 2: Evaluate antibodies on both spam and ham
        spam_scores = [sum(evaluate_antibody(antibody, antigen) for antigen in spam_antigens)
               for antibody in population]

        ham_scores = [sum(evaluate_antibody(antibody, antigen) for antigen in ham_antigens)
              for antibody in population]


        # Combine the scores from both spam and ham for the final evaluation (you can apply a weighting factor)
        combined_scores = [spam_score + ham_score for spam_score, ham_score in zip(spam_scores, ham_scores)]

        # Step 3: Clone and mutate best antibodies based on combined scores
        top_antibodies = [antibody for _, antibody in sorted(zip(combined_scores, population), reverse=True)[:population_size // 2]]
        cloned_antibodies = clone_antibodies(top_antibodies, combined_scores)

        # Step 4: Mutate cloned antibodies
        mutated_population = [mutate_antibody(antibody) for antibody in cloned_antibodies]

        # Step 5: Keep some random antibodies to maintain diversity
        random_antibodies = random.sample(population, population_size // 5)  # Keep 20% of random ones

        # New population is a combination of mutated antibodies and random ones
        population = mutated_population + random_antibodies

    return population



def train_csa(spam_emails, easy_ham_emails, num_generations=10, population_size=50):
    """
    Handles the full training pipeline, ensuring train.py doesn't need imports.
    
    :param spam_emails: Raw spam email texts.
    :param easy_ham_emails: Raw ham email texts.
    :param num_generations: Number of training iterations.
    :param population_size: Population size.
    :return: Trained antibodies.
    """
    spam_antigens, ham_antigens = initialize_antigens(spam_emails, easy_ham_emails)
    return train(spam_antigens, ham_antigens, num_generations, population_size)
def classify_email_with_antibodies(email_antigen, trained_antibodies_spam, trained_antibodies_ham):
    """
    Classifies an email using trained spam and ham antibodies.

    :param email_antigen: Encoded email content as an antigen (word frequency dict).
    :param trained_antibodies_spam: List of trained spam antibodies.
    :param trained_antibodies_ham: List of trained ham antibodies.
    :return: "spam" or "ham".
    """
    if not trained_antibodies_spam or not trained_antibodies_ham:
        return "unknown"  # No antibodies trained, can't classify

    # Compute similarity scores separately for spam and ham
    spam_scores = [evaluate_antibody(antibody, email_antigen) for antibody in trained_antibodies_spam]
    ham_scores = [evaluate_antibody(antibody, email_antigen) for antibody in trained_antibodies_ham]

    # Get the highest similarity scores for each class
    max_spam_score = max(spam_scores) if spam_scores else 0
    max_ham_score = max(ham_scores) if ham_scores else 0

    print(f"Max spam similarity: {max_spam_score}, Max ham similarity: {max_ham_score}")  # Debugging

    # Classify based on which similarity is higher
    return "spam" if max_spam_score > max_ham_score else "ham"





def predict_email(email_text, trained_antibodies_spam, trained_antibodies_ham):
    """
    Classifies a new email using trained spam and ham antibodies.

    :param email_text: Email text to classify.
    :param trained_antibodies_spam: List of trained spam antibodies.
    :param trained_antibodies_ham: List of trained ham antibodies.
    :return: "spam" or "ham".
    """
    email_antigen = encode_emails_as_antigens([email_text])[0]  # Convert email text to antigen

    return classify_email_with_antibodies(email_antigen, trained_antibodies_spam, trained_antibodies_ham)
