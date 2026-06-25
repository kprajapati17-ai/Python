# 1) write recursive function to convert decimal into binary 
# 1) write recursive function to convert decimal into octal
# 1) write recursive function to convert decimal into hexadecimal
# Find sum of digits of a number
# Print table of a number using recursion
def toBinary(num):
    if num>0:
        rem = num % 2
        num = num // 2
        toBinary(num)
        print(rem,end="")

n = int(input("Enter Number:"))
toBinary(n)

def toOctal(num):
    if num>0:
        rem = num % 8
        num = num // 8
        toOctal(num)
        print(rem,end="")

n = int(input("Enter Number:"))
toOctal(n)

def toHexa(num):
    if num>0:
        rem = num % 16
        num = num // 16
        toHexa(num)
        if rem == 10:
            print("A",end="")
        elif rem == 11:
            print("B",end="")
        elif rem == 12:
            print("C",end="")
        elif rem == 13:
            print("D",end="")
        elif rem == 14:
            print("E",end="")
        elif rem == 15:
            print("F",end="")
        else:
            print(rem,end="")
 


n = int(input("Enter Number:"))
toHexa(n)

def sum_d(num):
    s = 0
    if num>0:
        rem = num % 10
        num = num // 10
        s = rem + sum_d(num)
    return s

d = sum_d(1234)
print(d)

def ptable(num,i=1):
    if i > 10:
       return
    print(f"{i} * {num} = {i*num}")
    ptable(num,i+1) 

ptable(10)