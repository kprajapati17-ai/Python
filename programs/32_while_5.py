# 4   0    1   1   2   3   5   8   13  .... 100

num = 0
step = 1

while num <=100:
    c = num + step
    num = step
    step = c
    print(num,end=" ")