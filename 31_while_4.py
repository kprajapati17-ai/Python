# 3   1    -8   27  -64  .....    1000

num = 1

while num<=10:
    cube = num * num * num
    if num % 2 ==0:
        cube = 0-cube
    print(cube,end=" ")
    num = num + 1

