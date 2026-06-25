from itertools import zip_longest

balance = 1000
def update_balance(amount):
    global balance
    balance = balance + amount
di = []
wi = []
while True:
    print("\n1 Deposit amount")
    print("2 Withrow amount")
    print("3 Check balance")
    print("4 Check Trasaction")
    print("0 exit ")
    ch = int(input("Enter Your Choise:"))

    if ch==1:
        a = int(input("Enter Amount:"))
        update_balance(a)
        di.append(a)
    elif ch==2:
        a = int(input("Enter Amount:"))
        wi.append(a)
        update_balance(-a) 
    elif ch==3:
        print(f"balance is:{balance}") 
    elif ch==4:
        for i,j in zip_longest(wi,di):
            print(f"Withrow amount:{i}")    
            print(f"Deposit amount:{j}")  

        print(f"balance is:{balance}") 
    elif ch==0:
        print("good by")
        break
    else:
        print("invalid Number")

print("end of program")

       
