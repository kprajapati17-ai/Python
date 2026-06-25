# 2) write a program to accept month number from user and display how many days month has. 
#     input : 1 output : this month has 31 days 
#     input : 4 output : this month has 30 days 


month = int(input("Enter month number (1-12): "))

if month==1 or  month==3 or  month==5 or  month==7 or  month==8 or  month==10 or month==12:
    print("this month has 31 days ") 
elif month==4 or  month==6 or  month==9 or month==10: 
    print("this month has 30 days")
elif month==2: 
    print("this month has 28/29 days")
else:
      print("invalid")