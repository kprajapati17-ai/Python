import spacy
import re
from spacy.language import Language
from spacy.tokens import Doc
from bad_words import L1

nlp = spacy.load("en_core_web_sm")

Doc.set_extension("Is_Adult", default=False)

def Check_Adult(text: str)-> bool:

    text = text.lower()

    for item in L1:
        pattern = r'\b' + re.escape(item.lower()) + r'\b'
        if re.search(pattern, text):
            # print("foundded,",pattern)
            return True

    return False

@Language.component("Find_Is_Adult")
def Find_Is_Adult(doc):
    doc._.Is_Adult = Check_Adult(doc.text)
    return doc

nlp.add_pipe("Find_Is_Adult", last=True)


text = """
The website was marked as NSFW because it contained adult-only content. The article discussed pornography, nudity, escort services, prostitution, erotic magazines, lingerie advertisements, and adult movies. Users were warned that the platform was intended only for people above 18 years of age."""


doc = nlp(text)


if doc._.Is_Adult:
    print("This Content Is Adult")
else:
    print("This Content Is Safe")
   

