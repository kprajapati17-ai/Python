# 2) create function that returns count of negative numbers from given number of argument 

def negitive_count(*num):
    ne = 0
    list = []
    for i in num:
        if i<0:
            ne = ne +1
            list.append(i)
    return ne,list

number,l = negitive_count(2,4,-56,78,-4,3,-9,0,1,-3,-7)        

print("count:",number,"and","negitive number :",l)