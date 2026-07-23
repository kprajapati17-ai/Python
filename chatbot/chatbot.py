# chatbot.py
# Core matching engine for the Easy Learn Academy Chatbot.

import preprocessing
import knowledge_base

def _match_keyword(keyword, words, cleaned_question):
    """
    Helper function to check if a keyword (list or string) matches the user's input.
    """
    if isinstance(keyword, list):
        # Composite matching: check if ALL words in the list are in user question words
        for word in keyword:
            if word not in words:
                return False
        return True
    elif isinstance(keyword, str) and " " in keyword:
        # Multi-word string phrase matching: check if phrase is in question or all its tokens match
        if keyword in cleaned_question:
            return True
        phrase_words = keyword.split()
        for word in phrase_words:
            if word not in words:
                return False
        return True
    else:
        # Single keyword matching: check if keyword is strictly in user question word tokens
        return keyword in words


def get_topics_sorted_by_priority():
    """
    Retrieves knowledge topics sorted by priority (1 = Highest priority).
    Supports both new structured dict 'topics' and legacy flat dict structures.
    """
    raw_kb = knowledge_base.knowledge
    
    if isinstance(raw_kb, dict) and "topics" in raw_kb:
        topics_dict = raw_kb["topics"]
    else:
        topics_dict = raw_kb

    sorted_topics = []
    for topic_name, data in topics_dict.items():
        priority = data.get("priority", 99) if isinstance(data, dict) else 99
        sorted_topics.append((priority, topic_name, data))
        
    # Sort by priority number ascending (1, 2, 3...)
    sorted_topics.sort(key=lambda x: x[0])
    return sorted_topics

def get_response(user_question):
    """
    Cleans the input question, applies spelling correction, and evaluates
    keyword matches ordered by topic priority:
    Pass 1: Multi-word phrase or composite matches (ordered by priority)
    Pass 2: Single-word keyword matches (ordered by priority)
    """
    cleaned_question = preprocessing.clean_text(user_question)
    
    if not cleaned_question:
        return "Please ask a question so I can assist you!"
    
    # Apply lightweight offline spelling correction to recognize typos
    corrected_question = preprocessing.correct_spelling(cleaned_question)
    words = corrected_question.split()
    sorted_topics = get_topics_sorted_by_priority()
    
    # PASS 1: Check multi-word phrase or composite keywords ordered by topic priority
    for priority, topic_name, data in sorted_topics:
        keywords = data.get("keywords", []) if isinstance(data, dict) else []
        for keyword in keywords:
            if isinstance(keyword, list) or (isinstance(keyword, str) and " " in keyword):
                if _match_keyword(keyword, words, corrected_question):
                    return data.get("answer", "")

    # PASS 2: Check single-word keywords ordered by topic priority
    for priority, topic_name, data in sorted_topics:
        keywords = data.get("keywords", []) if isinstance(data, dict) else []
        for keyword in keywords:
            if isinstance(keyword, str) and " " not in keyword:
                if _match_keyword(keyword, words, corrected_question):
                    return data.get("answer", "")
                
    # Fallback response if no keywords match
    return "Sorry, I don't have information about that yet. Feel free to call us at 9662512857 or visit https://theeasylearnacademy.com/ for quick inquiry!"



