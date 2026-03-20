#write a program to findout & display only positive value from the list using for loop
#task count positive and negative values and display it after for loop 
list = [12, -45, 7, -3, 89, -22, 0, 34, -9, 56] #list
p_count = 0
n_count = 0
zero = 0
for i in list:
    if i > 0:
        print(i)
        p_count = p_count + 1
    elif i < 0:    
        print(i)
        n_count = n_count + 1
    else:
        zero = zero  + 1

print("positive values count is:",p_count)
print("negative values count is:",n_count)
print("zero values count is:",zero)