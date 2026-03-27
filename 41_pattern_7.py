#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
'''first logic'''
c =1
for row in range(4):
    for sp in range(row,4):
        print(" ",end="")
    for st in range(0,c):
        print("*",end=" ") 
    print("")     
    c = c+ 1

c1 =5
for row in range(5,0,-1):
    for sp in range(row,5):
        print(" ",end="")
    for st in range(0,c1):
        print("*",end=" ") 
    print("")     
    c1 = c1 - 1 

"""second logic

for i in range(9):

    if i < 5:
        st = i + 1 
    else:
        st = 9 - i

    for sp in range(5-st):
        print(" ",end="")
    for st in range(st):
        print("*",end=" ") 
    print(" ") """
 

#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *
'''first logic'''
print("")  
print("")  
print("") 

c =1
for row in range(4):
    for sp in range(row,4):
        print(" ",end="")
    for st in range(0,c):
        if st==0 or st==c-1:
             print("*",end=" ") 
        else:
             print(" ",end=" ") 
 
    print("")     
    c = c+ 1

c1 =5
for row in range(5,0,-1):
    for sp in range(row,5):
        print(" ",end="")
    for st in range(0,c1):
        if st==0 or st==c1-1:
             print("*",end=" ") 
        else:
             print(" ",end=" ") 
    print("")     
    c1 = c1 - 1 