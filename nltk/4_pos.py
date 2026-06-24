import nltk

from nltk.tokenize import word_tokenize

text = "The quick brown fox jumps over the lazy dog."

tokens = word_tokenize(text)

tags = nltk.pos_tag(tokens)

print("Word\tPOS")
print("-" * 20)

for w,t in tags:
    print(f"{w}\t{t}")