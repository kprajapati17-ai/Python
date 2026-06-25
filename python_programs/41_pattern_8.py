"""
* * * * * * *
*           *
*     *     *
*           *
* * * * * * *
"""

c =1
for i in range(5):
    for j in range(7):
        if j==0 or i == 0 or j==6 or i == 4:
            print("*",end=" ")
        elif i==2 and j==3:
            print("*",end=" ")
        else:  
            print(" ",end=" ")  
    print(" ")    