import pandas as pd

state_city_count = {
    "Andhra Pradesh": 123,
    "Arunachal Pradesh": 33,
    "Assam": 97,
    "Bihar": 139,
    "Chhattisgarh": 182,
    "Goa": 14,
    "Gujarat": 348,
    "Haryana": 154,
    "Himachal Pradesh": 59,
    "Jharkhand": 57,
    "Karnataka": 317,
    "Kerala": 93,
    "Madhya Pradesh": 476,
    "Maharashtra": 413,
    "Manipur": 51,
    "Meghalaya": 24,
    "Mizoram": 23,
    "Nagaland": 39,
    "Odisha": 116,
    "Punjab": 166,
    "Rajasthan": 216,
    "Sikkim": 9,
    "Tamil Nadu": 649,
    "Telangana": 158,
    "Tripura": 20,
    "Uttar Pradesh": 762,
    "Uttarakhand": 115,
    "West Bengal": 129
}

s1 = pd.Series(state_city_count, name="Number of Cities")

print(s1)