import re 

def get_mobile_numbers(text: str)-> list:

    pattern = r'(?:\+91[\-\s]?)?[6-9]\d{9}\b'
    
    mobile_numbers = re.findall(pattern,text)

    return mobile_numbers