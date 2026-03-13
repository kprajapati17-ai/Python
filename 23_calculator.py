# 1) write a program to accept 2 number from user. and accept choice for operations.
# operations will be addition, subtraction, multiplication, division
#  do operation and display result as per user choice using switch statements.

num1 = int(input("Enter 1st No:"))
num2 = int(input("Enter 2ed No:"))

while True:

    print("1 SUM ")
    print("2 SUB ")
    print("3 DIV ")
    print("4 MUL ")
    print("5 EXIT ")

    ch = int(input("Enter Choice:"))

    if ch==1:
        print("SUM:",num1+num2)
    elif ch==2:
        print("SUB:",num1-num2)
    elif ch==3:
        print("DIV:",num1/num2)
    elif ch==4:
        print("MUL:",num1*num2)
    elif ch==5:
       exit()
    else:
        print("Invaid")
        
    
