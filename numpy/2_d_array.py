import numpy as np 

data = [[10, 20, 30], [40, 50, 60]]
array_2d = np.array(data)
print(array_2d)
print("Shape ",array_2d.shape)

print(array_2d[0][0])

#update
array_2d[0][0] = 1000
print(array_2d)