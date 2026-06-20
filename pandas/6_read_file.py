import pandas as pd

population = {
    "Gujarat":72,
    "Maharashtra":125,
    "Punjab":31,
    "Goa":16,
    "Rajasthan":82
}

s = pd.Series(population,name="Population")

print(s)

print("Index",s.index)

print("Values",s.values)

print("Size ",s.size)

print("Dimension",s.ndim)

print("Name",s.name)

print("Unique",s.is_unique)

print("Missing Values",s.hasnans)

print("Shape",s.shape)

print("Data Type",s.dtype)