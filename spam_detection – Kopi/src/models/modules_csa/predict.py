import numpy as np

def predict_email(email, antibodies, threshold=0.5):
    """
    Predicts whether the email is spam or not based on the affinity with the antibodies.
    
    :param email: The email to be classified (raw text or list of words).
    :param antibodies: The population of antibodies (i.e., feature vectors).
    :param threshold: The threshold above which the email is classified as spam.
    :return: 'spam' or 'ham' (non-spam).
    """
    # Step 1: Encode the email as an antigen (feature vector)
    antigen = encode_emails_as_antigens([email])[0]  # Convert the email into a feature vector (antigen)
    
    # Step 2: Compute affinities between the email (antigen) and each antibody
    affinities = []
    for antibody in antibodies:
        affinity = evaluate_antibody(antibody, antigen)
        affinities.append(affinity)
    
    # Step 3: Make a prediction based on the highest affinity
    # We predict spam if the highest affinity is above the threshold, otherwise non-spam (ham)
    max_affinity = max(affinities)
    
    if max_affinity >= threshold:
        return 'spam'
    else:
        return 'ham'

