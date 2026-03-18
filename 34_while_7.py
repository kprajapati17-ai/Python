# 5.1 write a program to make sum of all digits in given amount 
#     input : 12345 process 1 + 2 + 3 + 4 + 5 output = 15
      

n = int(input("Enter Any Number:"))
sum = 0
while n > 0 :
    rem = n % 10
    sum = sum + rem 
    n = n // 10
print("full number sum is:",sum) 