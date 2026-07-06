import spacy
import re
from spacy.language import Language
from spacy.tokens import Doc

nlp = spacy.load("en_core_web_sm")

Doc.set_extension("Coordinates", default=[])

def get_coordinates(text):
    pattern = r'[-+]?\d{1,2}\.\d+\s*,\s*[-+]?\d{1,3}\.\d+'
    return re.findall(pattern, text)

@Language.component("FetchCoordinates")
def FetchCoordinates(doc):
    doc._.Coordinates = get_coordinates(doc.text)
    return doc

nlp.add_pipe("FetchCoordinates", last=True)

text = """
Some famous locations:

Rajkot : 22.3039, 70.8022
Ahmedabad : 23.0225, 72.5714
New Delhi : 28.6139, 77.2090
Mumbai : 19.0760, 72.8777
London : 51.5074, -0.1278
New York : 40.7128, -74.0060
Sydney : -33.8688, 151.2093
Tokyo : 35.6762, 139.6503

Invalid Coordinates:
123.456, 789.123
abc, xyz
12,34
"""

doc = nlp(text)

print("Latitude and Longitude:")
for coordinate in doc._.Coordinates:
    print(coordinate)