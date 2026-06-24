from gensim.models import Word2Vec

data = [
    ["student","school","teacher","class","book","pen","exam","result"],
    ["doctor","hospital","patient","medicine","nurse","operation"],
    ["engineer","computer","python","coding","software","program"],
    ["farmer","field","crop","tractor","rain","harvest"]
]

model = Word2Vec(
    data,
    vector_size=20,
    window=5,
    min_count=1,
    epochs=500,
    sg=1
)

print("Vocabulary")
print(model.wv.index_to_key)

print()

print("Similar to Teacher")
print(model.wv.most_similar("teacher"))

print()

print("Similar to Python")
print(model.wv.most_similar("python"))

print()

print("Similar to Farmer")
print(model.wv.most_similar("farmer"))