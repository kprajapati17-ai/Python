# 9   write a program to findout whether given number is palindrome 
#     input : 12321 output 12321 this is palindrome
#     input : 12345 output 54321 this is not palindrome


# palindrome or not

# n =int(input("Enter N:"))
# rev =n
# s = 0
# while n > 0:
#    d = n % 10
#    s = s*10 + d
#    n = n//10

# print(s)

# if rev == s:
#     print(f"{s} is palindrome Number")
# else:
#    print(f" {s} is Not palindrome Number")


# 10  write a program to display given amount into words 
#     input : 12345 output : one two three four five

words = ["zero","One", "Two", "Three", "Four", "Five","Six", "Seven", "Eight", "Nine", "Ten"]

n =int(input("Enter N:")) 
s =[]
while n > 0:
    rem = n % 10
    s.insert(0,words[rem])
    # s.append(words[rem])
    n = n//10
    
print(" ".join(s))
