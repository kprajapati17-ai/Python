import nltk

from nltk.corpus import brown

print("BROWN CORPUS")
print("=" * 60)

# Show Brown categories
print("\nAvailable Categories:")
print(brown.categories())

# Read News Category
news = brown.words(categories="news")

print("\nTotal Words in News Category :", len(news))

print("\nFirst 100 Words:")
print(news[:100])

print("\nFirst 10 Sentences:")
print(brown.sents(categories="news")[:10])