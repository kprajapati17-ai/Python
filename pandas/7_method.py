import pandas as pd

runs = [100, 35, 55, 69, 29, 38]

s1 = pd.Series(
    runs,
    index=[
        "Salil Arora",
        "Abhishek Sharma",
        "Ishan Kishan",
        "Heinrich Klaasen",
        "Nitish Kumar Reddy",
        "Travis Head"
    ]
)

print(s1)

print(s1.head(5))

print(s1.tail(3))

print(s1.to_list())

print(s1.to_dict())

print(s1.describe())

s2 = s1.astype("Int32")

print(s2)