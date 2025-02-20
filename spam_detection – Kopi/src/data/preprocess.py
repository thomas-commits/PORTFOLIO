import re
from bs4 import BeautifulSoup

def preprocess_email(email_tuple):
    """
    Preprocess an email by removing HTML tags and cleaning up the format.
    """
    category, email_content = email_tuple  # Unpack the category and content

    # Split content into lines, and extract the body after the header (if present)
    lines = email_content.split("\n")
    body = "\n".join(lines[lines.index("") + 1:]) if "" in lines else email_content

    # Check for a minimal HTML structure (for simplicity, we're looking for basic tags)
    if '<html' in body.lower() and '</html>' in body.lower():
        body = BeautifulSoup(body, "html.parser").get_text()  # Only process if HTML-like content

    # Clean up extra whitespaces and empty lines
    body = re.sub(r'\s+', ' ', body).strip()

    return category, body  # Return the category and cleaned body content
