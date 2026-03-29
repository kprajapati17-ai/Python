#write a program to convert given amount into words 
# input : 12345
# output : one two three four five 

num = ['zero','first','second','three','four','five','six','seven','eight','nine']

n = int(input("Enter Any Number:"))
ch = []
while n > 0:
    reminder = n % 10
    ch.insert(0,num[reminder])
    n = n // 10
print((" ".join(ch)))
