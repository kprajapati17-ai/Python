import math
# #example of map and lambda function 
numbers = [5, -3, 12, 7, -8, 0, 19, -2, 4, 11, -6, 8, -1, 14, -9, 3, 6, -4, 10, -7]
print("original list ",numbers)

# #define lambda using map to convert negative numbers into positive numbers 
positive_numbers = map(lambda num: int(math.fabs(num)),numbers)
print(list(positive_numbers))

list1 = [2, 5, 8, 11, 14, 17, 18, 23, 26, 29]
list2 = [1, 7, 6, 9, 12, 15, 20, 25, 29, 45]

print(list1)
print(list2)
#define lambda using map to that return largest value at each and every position in two list 
list3 = map(lambda num1,num2: num1 if num1>num2 else num2,list1,list2)
print(list(list3))

#example of filter 
countries = [
    "India", "Finland", "Pakistan", "Australia", "Brazil",
    "Thailand", "Iceland", "Germany", "Kazakhstan", "Italy",
    "Poland", "Somalia", "Japan", "New Zealand", "Canada",
    "Uzbekistan", "Argentina", "Netherlands", "Sri Lanka", "Switzerland",
    "Ireland", "Bangladesh", "Norway", "Denmark", "Afghanistan",
    "Malaysia", "Colombia", "Greenland", "Nepal", "Swaziland",
    "Mongolia", "Indonesia", "England", "Scotland", "Estonia",
    "Latvia", "Lithuania", "Romania", "Bulgaria", "Serbia",
    "Croatia", "Slovakia", "Slovenia", "Armenia", "Georgia",
    "Ethiopia", "Albania", "Austria", "Belgium", "Mexico"
]
print(countries)
lands = list(filter(lambda item: 'land' in item,countries))
print(lands)

# #task 
# # filter countries whose name ends with stan
stan = list(filter(lambda item: 'stan' in item,countries))
print(stan)
# # filter countries whose name ends with ia 
ia = list(filter(lambda item: 'ia' in item,countries))
print(ia)
# 5) write a program that will return reverse of 2 digit numbers passed via list. use map function 


numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# print(sorted(numbers[4]))
rev = map(lambda num:(num % 10) * 10 + (num//10),numbers)
print(list(rev))
# 8) use map function to findout binary of each number in list 
#     [10,20,40,80,100]



def toBinary(num):
    if num > 0:
        rem = num % 2
        num = num // 2
        return toBinary(num) + str(rem)  # Return the reversed binary as string
    else:
        return ""

rev = map(toBinary,numbers)
print(list(rev))