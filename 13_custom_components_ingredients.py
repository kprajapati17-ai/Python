import spacy
import re
from spacy.language import Language
from spacy.tokens import Doc
from indian_ingredients import ingredients 

nlp = spacy.load("en_core_web_sm")

Doc.set_extension("Ingredients", default=[])

def get_ingredients(text: str)-> list:
        
        found_ingredients =[]

        text = text.lower()

        for item in ingredients:
                    pattern = r'\b' + re.escape(item.lower()) + r'\b'

                    if re.search(pattern, text, re.IGNORECASE):
                        found_ingredients.append(item)

        return found_ingredients

@Language.component("FetchIngredients")
def FetchIngredients(doc):
    doc._.Ingredients = get_ingredients(doc.text)
    return doc

nlp.add_pipe("FetchIngredients", last=True)


text = """
To prepare authentic Gujarati Style Pav Bhaji, heat 3 tablespoons of butter and 1 tablespoon of oil in a large pan. Add 1 teaspoon of cumin seeds and sauté 2 finely chopped onions until they become golden brown. Add 1 tablespoon of ginger-garlic paste and 2 chopped green chilies, then cook for a minute. Add 3 chopped tomatoes and cook until they become soft. Now add 2 boiled potatoes, 1 cup of cauliflower, ½ cup of green peas, ½ cup of capsicum, and ½ cup of carrots. Add 1 teaspoon of turmeric powder, 2 teaspoons of red chili powder, 2 teaspoons of pav bhaji masala, 1 teaspoon of coriander powder, ½ teaspoon of cumin powder, 1 teaspoon of sugar, and salt to taste. Pour in 1 cup of water and cook until all the vegetables become soft. Mash the vegetables well using a potato masher, then add fresh coriander leaves, 1 tablespoon of butter, and 1 tablespoon of lemon juice. Mix everything thoroughly and simmer for 5 minutes. Toast the pav with butter until golden brown and serve the hot Gujarati Style Pav Bhaji with chopped onions, lemon wedges, fresh coriander leaves, and extra butter on top."""


doc = nlp(text)


print("\Ingredients:")
for item in doc._.Ingredients:
    print(item)