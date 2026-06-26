import mysql.connector as con

try:
    connect = con.connect(host='localhost',user='root',passwd='',database='project_1',port='3306')
    print("Connected successfully...")
except con.Error as er:
    print("Not Connected...")
    print(er.errno)
    print(er.msg)