# lambda function 
# 1) write a program to get area of triangle using lambda function 

base =int(input("Enter Base:"))
height = int(input("Enter height:"))

t_area = lambda base,height: 0.5 * base * height
print("area of triangle",t_area(base,height))


# 2) write a program to findout bmi of given weight and height of person 

Weight =int(input("Enter Weight (kg)​:"))
height = int(input("Enter height:"))

bmi = lambda Weight,height: Weight / ((height/100) ** 2)
print("BMI Is :",bmi(Weight,height))

# 3) write a program to findout largest number from 3 given number using lambda function 

n1 =int(input("Enter N1​:")) 
n2 =int(input("Enter N2​:")) 
n3 =int(input("Enter N3​:")) 

max_n = lambda n1,n2,n3: n1 if n1 > n2 and n1 > n3 else (n2 if n2 > n3 else n3)
print("MAX NUMBER OUT OF THREE NUMBER :",max_n(n1,n2,n3))

# 4) create lambda function which return simple interest of given amount, rate, year 

p =int(input("Enter amount​:")) 
r =int(input("Enter rate:")) 
y =int(input("Enter year:")) 

simple_interest = lambda p,r,y: (p * r * y) /100
print("simple interest :",simple_interest(p,r,y))

# 6) create lambda function that return true if city passed as 1st argument exist in list passed argument as 2nd argument, if city does not exist return false 
#     isCityExist('Bhavnagar',['Bombay','Baroda','rajkot']) # false
#     isCityExist('rajkot',['Bombay','Baroda','rajkot']) # true 

l1 = ['Bombay','Baroda','rajkot']
p =input("Enter city name:")
isCityExist = lambda l1,p: True if p in l1 else False

print("City Is Exist:",isCityExist(l1,p))
