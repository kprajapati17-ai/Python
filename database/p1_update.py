import connect as conn

sql ="update product set name=%s,price=%s,quantity=%s where pid=%s"

name = input("Enter Product Name:")
price=int(input("Enter Product Price:"))
quantity=int(input("Enter Product quantity:"))
id=int(input("Enter Product Id:"))

values=[name,price,quantity,id]

cursor = conn.connect.cursor()

cursor.execute(sql,values)

conn.connect.commit()

if cursor.rowcount !=0:
    print("Product data Updated..")
else:
    print("Product Data not found...")