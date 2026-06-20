# write a program to calculate Least Common Divisor, and Greatest common Divisor of given values and return it together 
import math
def getLcmGcd(*num):

    g = num[0]

    for i in num[1:]:
        g = math.gcd(g,i)

    l = num[0]
    for i in num[1:]:
        l = (l*i) // math.gcd(l,i)


    return print(f"GCD{num} = {g} \nLCM{num} ={l}")

getLcmGcd(20,10,5)


