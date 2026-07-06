import spacy
import re
from spacy.language import Language
from spacy.tokens import Doc
import spacy.checkmobile as mn

nlp = spacy.load("en_core_web_sm")

Doc.set_extension("MobileNumbers", default=[])

@Language.component("FetchMobileNumbers")
def FetchMobileNumbers(doc):
    doc._.MobileNumbers = mn.get_mobile_numbers(doc.text)
    return doc

nlp.add_pipe("FetchMobileNumbers", last=True)

text = """

Mobile Numbers:
9876543210
9123456789
+91 9876501234
+91-9988776655


Invalid Mobile Numbers:
1234567890
5555555555
98765
11111111111
"""

doc = nlp(text)


print("\nMobile Numbers:")
for number in doc._.MobileNumbers:
    print(number)