# 4) write a program that will return numbers which are divisible by 10 using filter function 
numbers = [10, 15, 20, 23, 30, 33, 40, 41, 50, 52, 60, 61, 70, 73, 80, 85, 90, 91, 100, 105]
print(numbers)

dev = filter(lambda n:n % 10 == 0,numbers)
print(list(dev))