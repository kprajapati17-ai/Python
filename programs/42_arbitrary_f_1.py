# create function that returns average of player score of all 11 players (arbitrary arguments)

def avg(*run):
    sum =0
    c =0
    for i in run:
        sum = sum + i
        c = c+1

    avgrage = sum/c

    return avgrage

a = avg(20,30,40,50)
print("avgerage:",a)
  
a = avg(20,30,40,50,30,100,49,55,33,23,50)
print("avgerage:",a)  


# sortcut 
def avg2(*run):
    return sum(run)/len(run)

a = avg2(20,30,40,50,60,70)
print("avgerage:",a)

a = avg2(50,50,40,50,50)
print("avgerage:",a)

