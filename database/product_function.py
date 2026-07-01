import connect as conn

def getPrice(id):

    sql="select price,quantity from product where pid = %s"

    data=[id]

    cursor = conn.connect.cursor(dictionary=True)

    cursor.execute(sql,data)

    table = cursor.fetchall()

    No_Of_Rows = len(table)

    if No_Of_Rows ==0:
        return 0
    else:
        return table[0]['price'],table[0]['quantity']
        

def show(table):
    print(f"{'ID':<10} {'NAME':<40} {'PRICE':<12} {'QUANTITY':<12}")
    print("-" * 80)

    count = 0

    for row in table:
        print(f"{row['pid']:<10} {row['name']:<40} {row['price']:<12} {row['quantity']:<12}")

        count += 1

        if count == 25:
            input("\nPress Enter To Continue...")
            count = 0




def SearchProduct():
    name = input("Enter Product Name:")
    
    sql = "SELECT pid,name,price,quantity FROM product where name like %s AND is_deleted = 0 order by pid desc"

    cursor = conn.connect.cursor(dictionary=True)

    cursor.execute(sql, (f"%{name}%",))

    table = cursor.fetchall()

    if len(table) == 0:
        print("\nProduct Not Found...")
        return
    
    show(table)




def ViewProduct():
    sql = "SELECT pid,name,price,quantity FROM product where is_deleted = 0 order by pid desc"

    cursor = conn.connect.cursor(dictionary=True)

    cursor.execute(sql)

    table = cursor.fetchall()

    if len(table) == 0:
        print("\nProduct Not Found...")
        return
    
    show(table)





def AddProduct():
    sql ="insert into product (name,price,quantity) values(%s,%s,%s)"

    name = input("Enter Product Name:")
    price=int(input("Enter Product Price:"))
    quantity=int(input("Enter Product quantity:"))

    values=[name,price,quantity]

    cursor = conn.connect.cursor()

    cursor.execute(sql,values)

    conn.connect.commit()

    print("Product data inserted..")





def UpdateProduct():

    sql ="update product set name=%s,price=%s,quantity=%s where pid=%s"

    id=int(input("Enter Product Id:"))
    name = input("Enter Product Name:")
    price=int(input("Enter Product Price:"))
    quantity=int(input("Enter Product quantity:"))

    values=[name,price,quantity,id]

    cursor = conn.connect.cursor()

    cursor.execute(sql,values)

    conn.connect.commit()

    if cursor.rowcount !=0:
        print("Product data Updated..")
    else:
        print("Product Data not found...")


def DeleteProduct():
    sql ="update product set is_deleted = 1 where pid=%s "

    id=int(input("Enter Product Id:"))

    values=[id]

    cursor = conn.connect.cursor()

    cursor.execute(sql,values)

    conn.connect.commit()

    if cursor.rowcount !=0:
        print("Product data Deleted..")
    else:
        print("Product Data not found...")