# pip install deep-translator  # Use this version for better stability
# example to convert english text into gujarati text 
from deep_translator import GoogleTranslator

text = GoogleTranslator(source='en', target='gu').translate("Prajapati Kailash B")
print(text)



def trans(*str):
    l = []
    for i in str:
        text = GoogleTranslator(source='en', target='gu').translate(i)
        l.append(text)

    return " ".join(l)

guj = trans("hy","hallo","car","watch","cricket","science")
print(guj)
