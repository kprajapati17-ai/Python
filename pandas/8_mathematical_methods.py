import pandas as pd

# Population (Approximate, in Millions)
population = {
    "Uttar Pradesh": 241,
    "Maharashtra": 125,
    "Bihar": 128,
    "West Bengal": 101,
    "Madhya Pradesh": 86,
    "Tamil Nadu": 78,
    "Rajasthan": 82,
    "Karnataka": 69,
    "Gujarat": 72,
    "Punjab": 31
}

# Create Series
s1 = pd.Series(population, name="Population (Millions)")

print("Original Series")
print(s1)

# 1. Absolute Value
print("\n1. Absolute Value")
print(s1.abs())

# 2. Minimum Population
print("\n2. Minimum Population")
print(s1.min())

# 3. Maximum Population
print("\n3. Maximum Population")
print(s1.max())

# 4. State with Minimum Population
print("\n4. State with Minimum Population")
print(s1.idxmin())

# 5. State with Maximum Population
print("\n5. State with Maximum Population")
print(s1.idxmax())

# 6. Total Number of States
print("\n6. Number of States")
print(s1.size)

# 7. Length
print("\n7. Length")
print(len(s1))

# 8. Sort by Population
print("\n8. Sort by Population")
print(s1.sort_values())

# 9. Sort by Population (Descending)
print("\n9. Sort by Population Descending")
print(s1.sort_values(ascending=False))

# 10. Sort by State Name
print("\n10. Sort by State Name")
print(s1.sort_index())

# 11. Reverse State Name Order
print("\n11. Reverse State Name Order")
print(s1.sort_index(ascending=False))

# 12. First Five States
print("\n12. First Five States")
print(s1.head())

# 13. Last Five States
print("\n13. Last Five States")
print(s1.tail())

# 14. Convert into List
print("\n14. List")
print(s1.to_list())

# 15. Convert into Dictionary
print("\n15. Dictionary")
print(s1.to_dict())

# 16. Statistical Summary
print("\n16. Describe")
print(s1.describe())

# 17. Data Type
print("\n17. Data Type")
print(s1.dtype)

# 18. Convert Data Type
print("\n18. Convert to Float")
print(s1.astype("float"))

# 19. Average Population
print("\n19. Average Population")
print(s1.mean())

# 20. Total Population
print("\n20. Total Population")
print(s1.sum())

# 21. Median Population
print("\n21. Median Population")
print(s1.median())

# 22. Standard Deviation
print("\n22. Standard Deviation")
print(s1.std())