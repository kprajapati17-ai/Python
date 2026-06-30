import numpy as np 

array1 = np.linspace(1.0,2.0,num=10)

array2, step = np.linspace(2,3,num=5,retstep=True,endpoint=False)

print(array1)

print(array2,step)