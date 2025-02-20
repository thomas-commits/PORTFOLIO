def encode_words(words, word_counts, email_list):
    """
    Encodes a list of words by counting how many times each word appears in
    the first 50 words in the emails within the email list. The counts are
    updated in the word_counts dictionary, counting each word only once per email.
    """
    for word in words:
        # Initialize word count if not already present in the dictionary
        if word not in word_counts:
            word_counts[word] = 0
        
        # Track unique words in the first 50 words of each email
        word_set = set()  # A set to track unique words per email
        
        for email in email_list:
            # Only consider the first 50 words of the email
            first_50_words = email.split()[:50]
            
            # Add word to the set if it appears in the first 50 words
            if word in first_50_words:
                word_set.add(word)
        
        # Add the word count for the current word
        word_counts[word] += len(word_set)
    
    return {word: word_counts[word] for word in words}

