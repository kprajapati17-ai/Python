import spacy
import knowledge_base as kb

greetings = [
    "hello", "hi", "hey",
    "good morning", "good afternoon", "good evening",
    "greetings", "welcome", "howdy", "good day",
    "morning", "gm",
    "nice to meet you", "pleased to meet you",
    "how are you", "how's it going", "how have you been",
    "what's up", "what's new", "how do you do",
    "long time no see", "glad to meet you",
    "it's a pleasure to meet you",
    "good to see you", "happy to see you",
    "welcome back", "hope you're doing well",
    "hope you are fine"
]

nlp = spacy.load("en_core_web_sm")


def is_greeting(text):

    text = text.lower().strip()

    clean_list = []

    for ch in text:

        if ch.isalnum() or ch.isspace():
            clean_list.append(ch)

    clean_text = "".join(clean_list)

    for greet in greetings:

        if greet in clean_text:
            return True

    return False


def preprocess(question):

    # Greeting Check
    if is_greeting(question):
        print("Bot : Hello! Nice to meet you 😊")
        return

    doc = nlp(question)

    best_answer = None
    highest_priority = -1

    for token in doc:

        for topic in kb.knowledge["topics"]:

            keywords = kb.knowledge["topics"][topic]["keywords"]
            priority = kb.knowledge["topics"][topic]["priority"]

            if token.text.lower() in keywords:

                if priority > highest_priority:

                    highest_priority = priority
                    best_answer = kb.knowledge["topics"][topic]["answer"]

    # Final Answer
    if best_answer:
        print("Bot :", best_answer)
    else:
        print("Bot : Sorry! I don't know the answer.")




print("Bot : Hello! I am your assistant.")
print("Type 'bye' to exit.\n")

while True:

    question = input("You : ")

    q = question.lower().strip()

    if q == "bye":
        print("Bot : Bye! Have a nice day ")
        break

    preprocess(question)