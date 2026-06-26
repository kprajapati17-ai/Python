import connect as conn

sql = "SELECT * FROM product"

cursor = conn.connect.cursor(dictionary=True)

cursor.execute(sql)

table = cursor.fetchall()

print(f"{'ID':<10} {'NAME':<40} {'PRICE':<12} {'QUANTITY':<12}")
print("-" * 80)

count = 0

for row in table:
    print(f"{row['pid']:<10} {row['name']:<40} {row['price']:<12} {row['quantity']:<12}")

    count += 1

    if count == 25:
        input("\nPress Enter To Continue...")
        count = 0