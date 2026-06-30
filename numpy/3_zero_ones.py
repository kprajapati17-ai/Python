import numpy as np 

array1 = np.zeros(5)

array2 = np.ones(10)

array3 = np.ones([5,3])

print(array1)
print(array2)
print(array3)
 
array1[0] = 10 

array2[1] = 120

array3[0][1] = 99

print("now let us display all array again")
print(array1,array2)
print(array3)

