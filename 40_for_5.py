#write a program to count vowels in given string using for loop
line = input("What is your name?")

c = 0
vowels = 'aioue'

for n in line:
    if n in vowels:
        c = c + 1

print(c)