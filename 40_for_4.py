#write a program to display only that countries whose name ends with land
countries = ["india","pakistan","afghanistan","kazakhstan","uzbekistan","turkmenistan","tajikistan","kyrgyzstan","malaysia","micronesia","indonesia","thailand","finland","iceland","switzerland","new zealand","ireland","netherlands","poland","england","scotland","russia","china","japan","nepal","bhutan","sri lanka","bangladesh","myanmar","cambodia","vietnam","laos","philippines","singapore","australia","canada","mexico","brazil","argentina","chile","peru","colombia"]
#task display and count those country whole name ends with stan using different for lop. display count after loop finish. 
#task display and count those country whose name ends with sia different for loop. display count after loop finish. 

for i in countries:
    if "land" in i:
        print(i,end=" ") 
print()
for i in countries:
    if "stan" in i:
        print(i,end=" ") 
print()
for i in countries:
    if "sia" in i:
        print(i,end=" ") 