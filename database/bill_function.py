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



