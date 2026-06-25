#concept of keyword arguments 
def getMerit(maths, science, english, history, drawing, computer):
    print(f"maths = {maths}, science = {science}, english = {english}, history = {history}, drawing = {drawing}, computer = {computer}")
    total = maths + science + english 
    average = total / 3
    maximum = max(maths, science, english, history, drawing, computer)
    minimum = min(maths, science, english, history, drawing, computer)
    return total,average,maximum,minimum
m = int(input("Enter marks for Maths: "))
s = int(input("Enter marks for Science: "))
e = int(input("Enter marks for English: "))
h = int(input("Enter marks for History: "))
d = int(input("Enter marks for Drawing: "))
c = int(input("Enter marks for Computer: "))
total, average,mx,mi = getMerit(
    history=h,
    drawing=d,
    computer=c,
    maths=m,
    science=s,
    english=e,   
)
print("total:",total,"average:",average,"maximum:",mx,"minimum:",mi)