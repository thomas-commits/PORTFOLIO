from src.models.modules_csa.initialization import encode_words

def encode_first_50_words(spam_emails, easy_ham_emails, hard_ham_emails):
    """
    Encodes the first 50 words of each email in each category and tracks their frequency
    of appearance across emails.
    """
    encoded_data = {}
    word_counts = {}  # Initialize the word_counts dictionary to track counts

    # Process spam emails (first 50 emails)
    if spam_emails:
        first_50_words_spam = []
        
        # Iterate over the first 50 spam emails (or as many as are available)
        for email in spam_emails[:5]:
            first_50_words_spam.extend(email.split()[:50])
        
        # Encode the combined list of first 50 words from the first 50 spam emails
        encoded_data["spam"] = encode_words(first_50_words_spam, word_counts, spam_emails)

    # Process easy ham emails (first 50 emails)
    if easy_ham_emails:
        first_50_words_easy_ham = []
        
        # Iterate over the first 50 easy ham emails (or as many as are available)
        for email in easy_ham_emails[:5]:
            first_50_words_easy_ham.extend(email.split()[:50])
        
        # Encode the combined list of first 50 words from the first 50 easy ham emails
        encoded_data["easy_ham"] = encode_words(first_50_words_easy_ham, word_counts, easy_ham_emails)

    # Process hard ham emails (only the first email in this case)
    if hard_ham_emails:
        first_50_words_hard_ham = hard_ham_emails[0].split()[:50]
        encoded_data["hard_ham"] = encode_words(first_50_words_hard_ham, word_counts, hard_ham_emails)

    return encoded_data
