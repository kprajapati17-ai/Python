import connect as conn

sql ="delete from product where pid=%s"

id=int(input("Enter Product Id:"))

values=[id]

cursor = conn.connect.cursor()

cursor.execute(sql,values)

conn.connect.commit()

if cursor.rowcount !=0:
    print("Product data Deleted..")
else:
    print("Product Data not found...")