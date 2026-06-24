from sklearn.feature_extraction.text import CountVectorizer

data = [
    "The cat sat on the mat",
    "The dog sat on the log",
    "The cat chased the mouse",
    "The dog chased the cat"
]

c = CountVectorizer()

result = c.fit_transform(data)

print("Vocab__",c.vocabulary_)

print(result.toarray())