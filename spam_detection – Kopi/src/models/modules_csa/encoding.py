from collections import Counter

def encode_emails_as_antigens(emails):
    # List to store the antigens (which will be dictionaries of word occurrences)
    antigens = []
    
    for email in emails:
        # Tokenize email content into individual words (if email is raw text)
        if isinstance(email, str):  # In case email is a raw string, split it into words
            words = email.split()  # This will split by whitespace into words
        else:
            words = email  # If email is already a list of words, use it directly
        
        # Count occurrences of each word using Counter
        word_counts = dict(Counter(words))  # Count occurrences of each word
        
        # Add the word count dictionary as an antigen
        antigens.append(word_counts)
    
    return antigens
