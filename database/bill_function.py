import connect as conn
import product_function as pf

def AddBill():

    pf.ViewProduct()

    id = input("Enter Product id:")

    result = pf.getPrice(id)

    if isinstance(result,tuple)==False and result==0:
        print("Product not found")
    else:
        price,stock = result
        quantity = int(input("Enter quantity:"))
        if quantity>stock:
                print(f"Sorry, available stock is {stock} unit")
        else:
            sql = "insert into bill_items (productid,quantity,rate) VALUES (%s,%s,%s)"
            values = [id,quantity,price]
            cursor = conn.connect.cursor()

            cursor.execute(sql,values)

            conn.connect.commit()

            print("Item inserted")
    key = input("Press any key to continue")


def DeleteItemFromBill():
    DisplayBillItem()
    itemid = int(input("Enter Bill Item id to delete item from bill:=>"))
    sql = "delete from bill_items where id = %s"
    data = [itemid]

    cursor = conn.connect.cursor()

    cursor.execute(sql,data)

    conn.connect.commit()
    print("Item Deleted successfully")


def DisplayBillItem():

    sql = "select bi.id 'item_id', name, rate, bi.quantity 'quantity' from bill_items bi, product p where p.pid = productid and billid = 0 order by bi.id"

    cursor = conn.connect.cursor(dictionary=True)

    cursor.execute(sql)

    table = cursor.fetchall()

    if len(table) == 0:
        print("No Bill Item Found")
    else:
        print(f"{'item_id':<10} {'name':<60} {'rate':<10} {'quantity':<10} {'total':<12}")
        print("_" * 110)

        GrandTotal = 0
        ItemCount = 0

        for row in table:
            print(f"{row['item_id']:<10} {row['name']:<60} {row['rate']:<10} {row['quantity']:<10} {row['quantity'] * row['rate']:<12}")

            ItemCount += 1
            GrandTotal += (row['quantity'] * row['rate'])

        print("_" * 110)
        print(f"No Of Items = {ItemCount:<58} Grand Total = {GrandTotal:12}")

    input("Press any key to continue...")

def SearchItemInBill():
    name = input("Enter Item(product) Name:")

    sql = "select bi.id 'item_id', name, rate, bi.quantity 'quantity' from bill_items bi, product p where p.pid = productid and billid = 0 and name like %s order by bi.id"

    cursor = conn.connect.cursor(dictionary=True)

    cursor.execute(sql, (f"%{name}%",))

    table = cursor.fetchall()

    if len(table) == 0:
        print("No Bill Item Found")
    else:
        print(f"{'item_id':<10} {'name':<60} {'rate':<10} {'quantity':<10} {'total':<12}")
        print("_" * 110)

        for row in table:
            print(f"{row['item_id']:<10} {row['name']:<60} {row['rate']:<10} {row['quantity']:<10} {row['quantity'] * row['rate']:<12}")

        print("_" * 110)

def GenerateBill():
    confirm = input("Are you sure? you want to generate bill (press y/Y)")
    if confirm.lower() == 'y':
        # Task 1 check is there any unbilled item / calculate total 
        # Task 2 reduce stock of each and every product added into bill_items 
        # Task 3 accept customer name, email, mobile 
        # Task 4 insert row into bill table
        # Task 4 update bill_item table billid field, use last row id of bill to update it

        #Task 1 
        sql ="select sum(rate * quantity) as total from bill_items where billid=0"
        cursor = conn.connect.cursor(dictionary=True)
        cursor.execute(sql)
        row = cursor.fetchone()
        total = row['total']

        if row['total']==0:
                print("No item found in bill")
        else:
            #Task 2 
            sql ="select productid,quantity from bill_items where billid=0"
            cursor.execute(sql)
            table = cursor.fetchall()

            for row in table:
                quantity = row['quantity']
                productid = row['productid']
                sql = "update product set quantity=quantity-%s where pid = %s"
                data = [quantity,productid]
                cursor.execute(sql,data)

            #Task 3
            name = input("Enter Customer Name:")
            mobile = input("Enter Mobile No:")
            email = input("Enter Email:")
            paymentmode = input("Enter Payment Mode (1=Cash, 2=Credit) :")

            sql = "insert into bill(customername,email,mobile,amount,paymentmode) values(%s,%s,%s,%s,%s)"

            data=[name,email,mobile,total,paymentmode]

            cursor.execute(sql,data)

            billid = cursor.lastrowid #get last inserted row id of bill table

             # Task 4
            sql = "update bill_items set billid=%s where billid=0"
            data = [billid]
            cursor.execute(sql,data)

            print("BILL has been generated successfully")
            conn.connect.commit()

    key = input("Press any to continue")

                

       




