import nltk

from nltk.corpus import gutenberg
# from nltk.corpus import brown

print("\nAvailable Books:")
print(gutenberg.fileids)

whitman = gutenberg.words("whitman-leaves.txt")

print("\nTotal Words in Whitman Book :", len(whitman))

print("\nFirst 100 Words:")
print(whitman[:100])

print("\nFirst 10 Sentences:")
print(gutenberg.sents("whitman-leaves.txt")[:10])
