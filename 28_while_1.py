# example of while loop 
# 1 2 4 7 11 16 22 29 37 ..... 100

count = 1
step = 1

while count <= 100:
    count = count + step
    step = step + 1
    print(count,end=" ")