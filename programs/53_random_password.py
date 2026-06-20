import random as rd
import string as st


letters = st.ascii_lowercase + st.ascii_uppercase + st.digits + "!@#$%^&*()_+-={}[]|\:;<>,.?/~"
digi = st.digits
size = len(letters) - 1

def password_generet(length=20):

    global letters,size
    password = []
    for c in range(0,length):
        password.append(letters[rd.randint(0,size)])

    return "".join(password)

print(password_generet())  

def getotp(length=6):
    otp =[]
    for i in range(0,length):
        otp.append(digi[rd.randint(0,9)])
    return "".join(otp)

print(getotp())

