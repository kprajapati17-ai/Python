# 1) write a program to create function calculate and return simple Interest of given amount, rate, year 


def simple_interest(amount,rate,year):
    interest = (amount * rate * year)/100
    return interest

amount = int(input("Enter Amount:"))
rate = int(input("Enter rate:"))
year = int(input("Enter year:"))

result = simple_interest(amount,rate,year)
print("SIMPLE INTEREST IS :",result)