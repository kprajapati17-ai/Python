    #  1) write a program to create function getinches which return total inches of given meter,foot and inches . *(here foot and inches are optional and their default value is 0) 
#     1 meter = 39.37 inches
#     1 foot = 12 inches

def getInches(meter,foot=0,inches=0):
    totalinche = (meter * 39.37) + (foot * 12) + inches 
    print(f"METER:{meter} ... FOOT:{foot}...INCHES:{inches}")
    return totalinche

m =float(input("Enter Meter:"))
f =float(input("Enter Foot:"))
i =float(input("Enter Inches:"))

tot = getInches(m,f,i)
print(f"TOTAL INCHES:{tot}")

tot = getInches(m,f)
print(f"TOTAL INCHES:{tot}")

tot = getInches(m)
print(f"TOTAL INCHES:{tot}")