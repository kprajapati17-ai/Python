# chatbot.py
# Core matching engine for the simple offline chatbot.

import preprocessing
import knowledge_base

def get_response(user_question):
    """
    Cleans the input question, checks for keyword matches in the knowledge base,
    and returns the corresponding answer.
    """
    # 1. Clean the user's question (lowercase and remove punctuation)
    cleaned_question = preprocessing.clean_text(user_question)
    
    # 2. Split the cleaned question into individual words
    words = cleaned_question.split()
    
    # 3. Loop through each topic in the offline knowledge base
    for topic, data in knowledge_base.knowledge.items():
        # Check each keyword associated with the topic
        for keyword in data["keywords"]:
            if isinstance(keyword, list):
                # Composite matching: check if ALL words in the list are in user question words
                match = True
                for word in keyword:
                    if word not in words:
                        match = False
                        break
                if match:
                    return data["answer"]
            else:
                # Single keyword matching: check if it is in user question words
                if keyword in words:
                    return data["answer"]
                
    # 4. Return fallback response if no keyword matched
    return "Sorry, I don't have information about that yet."
