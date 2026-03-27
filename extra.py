def moveZero(array):
    list1 =[]
    z = 0
    for i in array:
        if i != 0:
            list1.append(i)
        else:
            z = z + 1
    for i in range(z):        
        list1.append(0)
    print(list1)

n = [0,1,0,3,12]
moveZero(n)

