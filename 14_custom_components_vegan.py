import spacy
import re
from spacy.language import Language
from spacy.tokens import Doc
from vegan_no_vegan_list import vegan,non_vegan

nlp = spacy.load("en_core_web_sm")

Doc.set_extension("Is_Vegan", default=False)

def Check_Vegan(text: str)-> bool:
        
       is_vegan = True

       text = text.lower()

       for item in non_vegan:
           print(item)
           if item.lower() in text:
               print("foundedd",item)
               is_vegan = False
               break
                  

       return is_vegan

@Language.component("Find_Is_Vegan")
def Find_Is_Vegan(doc):
    doc._.Is_Vegan = Check_Vegan(doc.text)
    return doc

nlp.add_pipe("Find_Is_Vegan", last=True)


text = """
To prepare a delicious Vegan Vegetable Curry, heat 2 tablespoons of olive oil in a pan. Add 1 teaspoon of cumin seeds and sauté 2 finely chopped onions until golden brown. Add 1 tablespoon of minced garlic, 1 tablespoon of grated ginger, and 2 chopped green chilies. Add 3 chopped tomatoes and cook until soft. Mix in 1 teaspoon of turmeric powder, 2 teaspoons of coriander powder, 1 teaspoon of cumin powder, and 1 teaspoon of red chili powder. Add 2 chopped potatoes, 1 cup of cauliflower, 1 cup of carrots, 1 cup of green peas, and 1 cup of spinach. Pour in 2 cups of water and add salt to taste. Cover the pan and cook until the vegetables become tender. Finally, add fresh coriander leaves and lemon juice, mix well, and serve the hot vegan vegetable curry with steamed basmati rice."""


doc = nlp(text)


if doc._.Is_Vegan==True:
    print("Recipe Is Vegan")
else:
    print("Recipe Is Not Vegan")
   

