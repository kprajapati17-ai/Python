# 2) write a program to create function calculate and return compound Interest of given amount, rate, year 



def compound_interest(amount,rate,year):
    result = amount *(1 + rate/100) ** year
    ci = result - amount
    return ci,result

amount = int(input("Enter Amount:"))
rate = int(input("Enter rate:"))
year = int(input("Enter year:"))

ci,result = compound_interest(amount,rate,year)
print("AMOUNT IS :",result)
print("COMPOUND INTEREST IS :",ci)
