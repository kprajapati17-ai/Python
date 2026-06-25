# 5.2 write a program to findout only compound interest of given amount, rate, year 
amount =int(input("Enter amount:"))
rate =float(input("Enter rate:"))
year =float(input("Enter Year:"))
o_amount = amount
i = 1
while i <= year:
    intrest = amount * (rate/100)
    amount = amount + intrest
    print("Year=",i,"Amount =", amount)
    i = i + 1

compound_interest = amount - o_amount
print("Final Amount =", amount)
print("compound_interest",compound_interest)