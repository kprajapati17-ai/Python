from nltk.stem import WordNetLemmatizer

lemma = WordNetLemmatizer()

print("Verb Lemmatization")
print("--------------------")
print("Swimming  ->", lemma.lemmatize("swimming", pos="v"))
print("Reading   ->", lemma.lemmatize("reading", pos="v"))
print("Dancing   ->", lemma.lemmatize("dancing", pos="v"))

print("\nAdjective Lemmatization")
print("-----------------------")
print("Better    ->", lemma.lemmatize("better", pos="a"))
print("Quick     ->", lemma.lemmatize("quick", pos="a"))

print("\nAdverb Lemmatization")
print("--------------------")
print("Quickly   ->", lemma.lemmatize("quickly", pos="r"))
print("Sincerely ->", lemma.lemmatize("sincerely", pos="r"))