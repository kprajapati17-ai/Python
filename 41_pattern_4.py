'''
1
2 3
4 5 6
7 8 9 10
'''
c = 1
for row in range(1,5):
    for sp in range(0,row):
        print(c,end=" ")
        c = c+ 1
    print("")
