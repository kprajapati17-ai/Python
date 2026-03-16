date =int(input("Enter Date:"))
month =int(input("Enter Month:"))
year =int(input("Enter Year:"))

month_table =[0,3,3,6,1,4,6,2,5,0,3,5]

# step-1

step1 = date + month_table[month-1]

step1 = step1 % 7

# step2

yy = year % 100
yy = yy - (yy//28)*28
step2 = yy + (yy//4)

# step3

century_year = year//100

if century_year == 17:
    c = 4
elif century_year == 18:  
    c = 2 
elif century_year == 19:  
    c = 0 
elif century_year == 20:  
    c = 6 
elif century_year == 21:  
    c = 4 
else:
    c = 0

step3 = step2 + c

# step4

total = step1 + step3

total = total % 7

days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

print("DAY IS : ",days[total])