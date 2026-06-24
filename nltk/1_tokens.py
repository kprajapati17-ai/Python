import nltk
from nltk.tokenize import sent_tokenize,word_tokenize

nltk.download("punkt_tab")

text="""Natural Language Processing (NLP) is a branch of Artificial Intelligence that enables computers to understand, interpret, and generate human language.
It is widely used in applications such as chatbots, language translation, sentiment analysis, speech recognition, and text summarization.
By combining linguistics with machine learning and deep learning techniques, NLP helps machines communicate and interact with humans more effectively.
"""

Sentence = sent_tokenize(text)

Word = word_tokenize(text)

print("Sentence Tokenization:\n")

for item in Sentence:
    print(item)

print("\nWord Tokenization:\n")

print(Word)