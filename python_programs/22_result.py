# 4) 
# Write a program that takes a 5 subject marks from user. calculate total and average  and prints the grade using the following conditions:

# | avgntage | Grade |
# | ---------- | ----- |
# | 90–100     | A+    |
# | 80–89      | A     |
# | 70–79      | B     |
# | 60–69      | C     |
# | 50–59      | D     |
# | below 50   | Need to improve  |


sub1_mark = int(input("Enter English Mark:"))
sub2_mark = int(input("Enter Math Mark:"))
sub3_mark = int(input("Enter Gujrati Mark:"))
sub4_mark = int(input("Enter Hindi Mark:"))
sub5_mark = int(input("Enter Science Mark:"))

if sub1_mark>=0 and sub1_mark<=100 and sub2_mark>=0 and sub2_mark<=100 and sub3_mark>=0 and sub3_mark<=100 and sub4_mark>=0 and sub4_mark<=100 and sub5_mark>=0 and sub5_mark<=100:
    total = sub1_mark + sub2_mark + sub3_mark + sub4_mark + sub5_mark
    avg = total / 5
    print(f"Total Marks is :{total}")
    print(f"avgntage is :{avg}")
    if avg>=90:
        print("Grade A+")
    elif avg>=80:
         print("Grade A")   
    elif avg>=70:
         print("Grade B")
    elif avg>=60:
         print("Grade C") 
    elif avg>=50:
         print("Grade D") 
    else:
        print("need to improve")  
else:
     print("Invalid Marks")         