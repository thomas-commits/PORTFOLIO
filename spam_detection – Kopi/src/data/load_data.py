import os
import glob
from bs4 import BeautifulSoup

def load_all_emails(data_dir):
    """
    Load all email files from data_dir and its subdirectories.
    """
    emails = []

    # Iterate through the subdirectories (easy_ham, hard_ham, spam_2)
    for category in os.listdir(data_dir):
        category_path = os.path.join(data_dir, category)
        print(f"Checking category: {category_path}")

        # Check if it's a directory
        if os.path.isdir(category_path):
            # Now correctly navigate to the second level of subfolder (e.g., easy_ham/easy_ham)
            subfolder_path = os.path.join(category_path, category)  # Going one level deeper
            if os.path.isdir(subfolder_path):
                email_files = glob.glob(os.path.join(subfolder_path, "*"))  # Get all files in the folder
                print(f"Found {len(email_files)} files in {subfolder_path}")
                
                # Iterate over the files in the subfolder
                for file in email_files:
                    # Ensure that it's a file and not a directory
                    if os.path.isfile(file):
                        with open(file, "r", encoding="utf-8", errors="ignore") as f:
                            emails.append((category, f.read()))  # Store category and content as a tuple

    print(f"Total emails loaded: {len(emails)}")
    return emails
