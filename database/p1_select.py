import connect as conn

sql ="select * from product"



cursor = conn.connect.cursor()

cursor.execute(sql)

rows = cursor.fetchall()

for data in rows:
    print(data)