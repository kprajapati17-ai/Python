import pandas as pd
import numpy as np

print(pd.__version__)

run =[50,40,80,90,60,30]

s1 = pd.Series(run)
print(s1)

s2=pd.Series([22,33,44,55,66,77,88])
print(s2)

state_income = {"Sikkim": 677000, "Goa": 650000, "Delhi": 461000, "Telangana": 350000, "Karnataka": 330000, "Haryana": 325000, "Tamil Nadu": 315000, "Gujarat": 305000, "Maharashtra": 290000, "Kerala": 285000, "Andhra Pradesh": 245000, "Punjab": 200000, "Himachal Pradesh": 235000, "Mizoram": 220000, "Arunachal Pradesh": 215000, "Uttarakhand": 255000, "Rajasthan": 180000, "West Bengal": 165000, "Odisha": 175000, "Chhattisgarh": 155000, "Madhya Pradesh": 150000, "Assam": 130000, "Manipur": 105000, "Nagaland": 145000, "Meghalaya": 115000, "Tripura": 160000, "Jharkhand": 95000, "Uttar Pradesh": 90000, "Bihar": 60000}

s3 =pd.Series(state_income)
print(s3)

a1 = np.array([1000,2000,3000,4000,5000])
s4= pd.Series(a1,index=['kp','mp','jp','jp','dp'],name="expence")
print(s4)       