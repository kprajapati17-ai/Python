import pandas as pd

csv = pd.read_csv("marks.csv")
print(csv)


excel = pd.read_excel("marks.xlsx")
print(excel)

json = pd.read_json("marks.json")
print(json)