from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = [
    "running", "runs", "runner", "runners",
    "walked", "walking", "walks", "walker",
    "playing", "played", "plays", "player",
    "studying", "studied", "studies",
    "writing", "written", "writes", "writer"
]

print("Original Word\tStem Word")
print("-" * 30)

for w in words:
    print(f"{w}\t\t{ps.stem(w)}")