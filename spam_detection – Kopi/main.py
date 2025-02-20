import sys
from src.data.load_data import load_all_emails
from src.data.preprocess import preprocess_email
from src.models.csa_aggregator import encode_first_50_words

from src.models.ais_csa_aggregator import initialize_antigens
from src.models.ais_csa_aggregator import train_csa, predict_email, train  # Import from the corrected location

sys.stdout.reconfigure(encoding='utf-8')  # Ensure UTF-8 encoding for output

def print_email_samples(spam_emails, easy_ham_emails, hard_ham_emails):
    """
    Print samples from each email category.
    """
    print("First 3 Spam emails:")
    for email in spam_emails[:3]:
        print(email[:50])  # Show the first 50 characters of each email

    print("\nFirst 3 Easy Ham emails:")
    for email in easy_ham_emails[:3]:
        print(email[:50])  # Show the first 50 characters of each email

    print("\nFirst 3 Hard Ham emails:")
    for email in hard_ham_emails[:3]:
        print(email[:50])  # Show the first 50 characters of each email

if __name__ == "__main__":
    data_folder = "data"  # Path to the data folder

    # Load and preprocess emails
    raw_emails = load_all_emails(data_folder)
    processed_emails = [preprocess_email(email) for email in raw_emails]

    # Separate emails by category (Only necessary once)
    spam_emails = [email for category, email in processed_emails if category == 'spam_2']
    easy_ham_emails = [email for category, email in processed_emails if category == 'easy_ham']
    hard_ham_emails = [email for category, email in processed_emails if category == 'hard_ham']

    # Apply subset size (limit the number of emails, for example to 1000 emails per category)
    spam_emails = spam_emails[:17]
    easy_ham_emails = easy_ham_emails[:17]
    hard_ham_emails = hard_ham_emails[:1]
    import random

    # Apply subset size for prediction (Use up to 1389 emails)
    spam_emails_predict = spam_emails[:400]  # Ensure there are enough spam emails
    easy_ham_emails_predict = easy_ham_emails[:400]  # Ensure there are enough ham emails



    # Initialize antigen representations with the subset data
    spam_antigens, ham_antigens = initialize_antigens(spam_emails, easy_ham_emails)

    # Print examples for verification
    print("Example of spam-antigen:", spam_antigens[:2])
    print("Example of ham-antigen:", ham_antigens[:2])


    # Randomly select 5 spam emails and 5 ham emails (if available)
    num_spam = min(2, 1389)
    num_ham = min(2, 1389)

    random_spam_emails = random.sample(spam_emails_predict, num_spam) if spam_emails_predict else []
    random_ham_emails = random.sample(easy_ham_emails_predict, num_ham) if easy_ham_emails_predict else []

    # Train spam and ham antibodies separately
    trained_antibodies_spam = train_csa(spam_emails, easy_ham_emails)  
    trained_antibodies_ham = train_csa(easy_ham_emails, spam_emails)  

    # Predict and print results for spam emails
    print("\nPredictions for randomly selected **SPAM** emails:\n")
    for i, email in enumerate(random_spam_emails):
        prediction = predict_email(email, trained_antibodies_spam, trained_antibodies_ham)
        print(f"Spam Email {i+1}: {email[:250]}...")
        print(f"Prediction: {prediction}\n")

    # Predict and print results for ham emails
    print("\nPredictions for randomly selected **HAM** emails:\n")
    for i, email in enumerate(random_ham_emails):
        prediction = predict_email(email, trained_antibodies_spam, trained_antibodies_ham)
        print(f"Ham Email {i+1}: {email[:250]}...")
        print(f"Prediction: {prediction}\n")




    # Uncomment the following lines if you'd like to check dataset stats, sample emails, or encoded words
    '''
    # Print dataset stats (Number of emails in each category)
    print(f"Number of spam emails in subset: {len(spam_emails)}")
    print(f"Number of easy_ham emails in subset: {len(easy_ham_emails)}")
    print(f"Number of hard_ham emails in subset: {len(hard_ham_emails)}")

    # Print email samples (first 50 characters of first 3 emails in each category)
    print_email_samples(spam_emails, easy_ham_emails, hard_ham_emails)

    # Encode the first 50 words from the first 50 emails in each category
    encoded_words = encode_first_50_words(spam_emails, easy_ham_emails, hard_ham_emails)
    
    # Print encoded words for each category
    print("\nEncoded first words from the first 50 emails in each category:")
    for category, encoding in encoded_words.items():
        print(f"{category}: {encoding}")
    '''