# write a program to count words, vowel, consent,digit and symbols in given string

vowel = 'aioue'
v = 0
c = 0
digit ='1234567890'
d = 0
simbo ='!@#$%^&'
s = 0
line = input("Enter String :")

for i in line:

    if i in vowel:
        v = v + 1
    elif i in digit:
        d = d +1
    elif i in simbo:
        s = s +1
    else:
        c = c + 1    

print("vowel count:",v)

print("consent count:",c)

print("digit count:",d)

print("symbols count:",s)
