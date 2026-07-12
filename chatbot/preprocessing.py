# preprocessing.py
# This module performs simple text cleaning to help matching.

def clean_text(text):
    """
    Converts text to lowercase and removes basic punctuation.
    Example: "What is Python?" -> "what is python"
    """
    # 1. Convert text to lowercase and remove spaces from ends
    text = text.lower().strip()
    
    # 2. Define standard punctuation characters to remove
    punctuation = "?!.,:;()\"'"
    
    # 3. Replace each punctuation character with an empty string
    for char in punctuation:
        text = text.replace(char, "")
        
    return text
