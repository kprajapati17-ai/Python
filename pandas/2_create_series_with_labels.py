import pandas as pd

print(pd.__version__)

marks=[66,86,90,38,89]

s1 = pd.Series(marks,index=["Amit", "Neha", "Rahul", "Priya","dhruv"])

print(s1)

s2 = pd.Series(
    [42.3,41.0,41.0,39.0,38.5,38.0,35.0],
    index=[
        "Rajkot",
        "Surendranagar",
        "Kandla",
        "Ahmedabad",
        "Gandhinagar",
        "Bhavnagar",
        "Surat"
    ]
)

print(s2)