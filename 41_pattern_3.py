'''
        *
      * * 
    * * * 
  * * * *
* * * * *
'''

c = 1
for row in range(5,0,-1):
    for space in range(0,row):
        print(" ",end=" ")
    for est in range(0,c):
        print("*",end=" ") 
    c = c + 1   
    print()  