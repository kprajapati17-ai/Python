'''
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''
for row in range(5,0,-1):

    for sp in range(row,0,-1):
        print(sp,end=" ")  
        
    print()

'''
    1
   0 1
  1 0 1
 0 1 0 1
0 1 0 1 0 '''

c =2
for row in range(5):
    for sp in range(row,5):
        print(" ",end="")
    for st in range(1,c):
        if (row+st)%2==0:
            print("0",end=" ") 
        else:
            print("1",end=" ") 
       
    print("")
    c =c + 1