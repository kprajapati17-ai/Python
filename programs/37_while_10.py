
# 7   write a program to findout whether given number is prime number or not 
# 8   write a program to findout whether given number is perfect number or not 

# 1 prime number or not 
n =int(input("Enter N:"))

i = 1
c =0
while i<=n:
    if n%i==0:
       c = c + 1     
    i = i +1

if c == 2:
    print("Prime Number")
else:
   print("Not Prime Number")


# 2 perfect number or not

n1 =int(input("Enter N:"))

i = 1
s =0
while i<n1:
     if n1%i==0:
        s = s + i    
     i = i +1

print(s)
if s == n1:
    print("Perfect Number")
else:
   print("Not Perfect Number")