# example of while loop 
# 1 -4  9  -16 25 -36 49 -64 ..... 400 

num = 1
# step = num * num

while num <= 20:
    step = num * num
    if num%2==0:
        step = 0-step
    print(step,end=" ")
    num = num + 1    