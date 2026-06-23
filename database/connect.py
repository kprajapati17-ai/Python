import mysql.connector as con

try:
    connect = con.connect(host='localhost',user='root',passwd='',database='mkbu_stud',port='3306')
    print("Connected successfully...")
except con.Error as er:
    print("Not Connected...")
    print(er.errno)
    print(er.msg)