#     *
#    * *
#   * * *
#  * * * *
# * * * * *
c =1
for row in range(0,5):
    for sp in range(row,5):
         print(" ",end="")
    for st in range(0,c):
        print("*",end=" ")
    c = c+ 1
    print("")





# *  
# *  *  
# *  *  *
# *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *
# for row in range(1,6):
#     for st in range(0,row):
#         print("* ",end=" ")
    
#     print("")


# # c = 1
# for row in range(6,1,-1):
#     for sp in range(1,row):
#          print("* ",end=" ")
#     # c = c+1
#     print("")


#     *
#    * *
#   *   *
#  *     *
# * * * * *
c =1
for row in range(0,5):
    for sp in range(row,5):
         print(" ",end="")
    for st in range(0,c):
        if st==row or c==5 or st==0: 
         print("*",end=" ")
        else:
         print(" ",end=" ")
    c = c+ 1
    print("")

