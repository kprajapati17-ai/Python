# preprocessing.py
# This module performs text cleaning and lightweight offline spelling correction.

import difflib
import knowledge_base

# Global cached vocabulary list built from knowledge_base keywords
_VOCABULARY = None

def build_vocabulary(force_refresh=False):
    """
    Dynamically builds a vocabulary set of valid words from knowledge_base.py keywords.
    """
    global _VOCABULARY
    if _VOCABULARY is not None and not force_refresh:
        return _VOCABULARY

    vocab_set = {
        "what", "where", "when", "how", "who", "why", "tell", "give", "me", "is",
        "are", "do", "you", "about", "details", "info", "information", "syllabus",
        "fees", "fee", "duration", "time", "timings", "placement", "certificate",
        "admission", "course", "courses", "contact", "location", "address", "call"
    }

    raw_kb = getattr(knowledge_base, "knowledge", {})
    topics_dict = raw_kb.get("topics", raw_kb) if isinstance(raw_kb, dict) else {}

    for topic_name, data in topics_dict.items():
        if isinstance(data, dict):
            keywords = data.get("keywords", [])
            for kw in keywords:
                if isinstance(kw, str):
                    for word in kw.split():
                        cleaned_word = "".join(c for c in word.lower() if c.isalnum() or c == "+")
                        if len(cleaned_word) > 1:
                            vocab_set.add(cleaned_word)
                elif isinstance(kw, list):
                    for word in kw:
                        if isinstance(word, str):
                            cleaned_word = "".join(c for c in word.lower() if c.isalnum() or c == "+")
                            if len(cleaned_word) > 1:
                                vocab_set.add(cleaned_word)

    _VOCABULARY = list(vocab_set)
    return _VOCABULARY

def clean_text(text):
    """
    Converts text to lowercase, replaces slashes/hyphens with spaces,
    and removes basic punctuation while preserving '+' for C++.
    Example: "What is C/C++ & Python?" -> "what is c c++ python"
    """
    if not isinstance(text, str):
        text = str(text) if text is not None else ""
        
    # 1. Convert text to lowercase and remove leading/trailing whitespace
    text = text.lower().strip()
    
    # 2. Replace slashes and hyphens with spaces to separate words (e.g. C/C++ -> C C++)
    for char in "/-_":
        text = text.replace(char, " ")
    
    # 3. Define punctuation characters to remove (excluding '+' so 'c++' remains intact)
    punctuation = "?!.,:;()\"'@#$%^&*~`"
    for char in punctuation:
        text = text.replace(char, "")
        
    # 4. Collapse multiple consecutive spaces into a single space
    cleaned = " ".join(text.split())
    return cleaned

def correct_spelling(text, cutoff=0.70):
    """
    Automatically recognizes and fixes typos in words using Python's built-in difflib.
    Tolerates ~75-90% similar spelling mistakes (e.g. 'pythn' -> 'python', 'corse' -> 'course').
    """
    vocab = build_vocabulary()
    words = text.split()
    corrected_words = []

    for word in words:
        # Keep short words or exact vocabulary matches unchanged
        if len(word) <= 2 or word in vocab:
            corrected_words.append(word)
            continue

        # Look for closest match in vocabulary with similarity >= cutoff
        matches = difflib.get_close_matches(word, vocab, n=1, cutoff=cutoff)
        if matches:
            corrected_words.append(matches[0])
        else:
            corrected_words.append(word)

    return " ".join(corrected_words)


