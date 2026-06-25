    #  2) write a program to create function getGrams which return total grams of given  Ton, Kilo and grams . *(here kilo and grams are optional and their default value is 0) 
# 1 ton (tonne) = 1,000 kg
# 1 kg = 1,000 grams

def getGram(ton,kg=0,gram=0):
    totalGram = (ton * 1000 * 1000) + (kg * 1000) + gram 
    print(f"TON:{ton} ... KG:{kg}...GRAM:{gram}")
    return totalGram

t =int(input("Enter Ton:"))
k =int(input("Enter Kg:"))
g =int(input("Enter Gram:"))

tot = getGram(t,k,g)
print(f"TOTAL GRAMS:{tot}")

tot = getGram(t,k)
print(f"TOTAL GRAMS:{tot}")

tot = getGram(t)
print(f"TOTAL GRAMS:{tot}")