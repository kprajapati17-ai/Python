# 6   write a program to findout power of given base and exponent 

base =int(input("Enter base:"))
exponent =float(input("Enter exponent:"))
power = 1
while exponent > 0:
    power = power * base
    print(power)
    print(exponent)
    print()
    exponent = exponent - 1

print("POWER :",power)
