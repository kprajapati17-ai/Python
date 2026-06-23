import connect as conn

sql ="insert into product (name,price,quantity) values(%s,%s,%s)"

name = input("Enter Product Name:")
price=int(input("Enter Product Price:"))
quantity=int(input("Enter Product quantity:"))

values=[name,price,quantity]

cursor = conn.connect.cursor()

cursor.execute(sql,values)

conn.connect.commit()

print("Product data inserted..")