# write a program to findout minimum marks & subject name and maximum marks and subject name from given dictionary 
marks = {"Math": 88, "English": 75, "Science": 92, "History": 80, "Geography": 78, "Computer": 95}

max1 = marks['Math']
min1 = marks['Math']
sub1 =""
sub2=""
print(max1," ",min1)
for item in marks:
    if marks[item] > max1:
        max1 = marks[item]
        sub1 = item
    if marks[item]  < min1:
        min1 = marks[item]
        sub2 = item
print(f"{max1} in maxmum marks {sub1}")   
print(f"{min1} in minimum marks {sub2}")