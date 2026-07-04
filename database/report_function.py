import connect as conn


def displayReport(sql, params=None):

    cursor = conn.connect.cursor(dictionary=True)

    if params:
        cursor.execute(sql, params)
    else:
        cursor.execute(sql)

    table = cursor.fetchall()

    cursor.close()

    if len(table) == 0:
        print("\nNo Records Found")
        input("\nPress Enter To Continue...")
        return

    columns = list(table[0].keys())

    width = {}

    for col in columns:

        max_len = len(col)

        for row in table:

            if len(str(row[col])) > max_len:
                max_len = len(str(row[col]))

        width[col] = max_len + 3

    print()

    for col in columns:
        print(f"{col:<{width[col]}}", end="")

    print()

    print("-" * sum(width.values()))

    for row in table:

        for col in columns:

            print(f"{str(row[col]):<{width[col]}}", end="")

        print()

    print("-" * sum(width.values()))

    input("\nPress Enter To Continue...")




def DailyReport():

    sql = """
    SELECT COUNT(DISTINCT b.id) AS total_bills,
    COUNT(*) AS total_items,
    (SELECT SUM(amount)
    FROM bill
    WHERE DATE(billdate)=CURDATE()) AS total_bill_amount
    FROM bill b,bill_items bi
    WHERE b.id=bi.billid
    AND DATE(b.billdate)=CURDATE();
    """

    print("\n========== DAILY REPORT ==========\n")

    displayReport(sql)




def WeeklyReport():

    sql = """
    SELECT COUNT(DISTINCT b.id) AS total_bills,
    COUNT(*) AS total_items,
    (SELECT SUM(amount)
    FROM bill
    WHERE billdate>=CURDATE()-INTERVAL 6 DAY
    AND billdate<CURDATE()+INTERVAL 1 DAY)
    AS total_bill_amount
    FROM bill b,bill_items bi
    WHERE b.id=bi.billid
    AND b.billdate>=CURDATE()-INTERVAL 6 DAY
    AND b.billdate<CURDATE()+INTERVAL 1 DAY;
    """

    print("\n========== WEEKLY REPORT ==========\n")

    displayReport(sql)





def MonthlyReport():

    sql = """
    SELECT COUNT(DISTINCT b.id) AS total_bills,
    COUNT(*) AS total_items,
    (SELECT SUM(amount)
    FROM bill
    WHERE billdate>=CURDATE()-INTERVAL 29 DAY
    AND billdate<CURDATE()+INTERVAL 1 DAY)
    AS total_bill_amount
    FROM bill b,bill_items bi
    WHERE b.id=bi.billid
    AND b.billdate>=CURDATE()-INTERVAL 29 DAY
    AND b.billdate<CURDATE()+INTERVAL 1 DAY;
    """

    print("\n========== MONTHLY REPORT ==========\n")

    displayReport(sql)





def ProductReport():

    print("\n========== PRODUCT REPORT ==========\n")

    start_date = input("Enter Start Date (YYYY-MM-DD) : ")

    end_date = input("Enter End Date (YYYY-MM-DD) : ")

    sql = """
    SELECT
    p.pid,
    p.name,
    SUM(bi.quantity) AS sold_quantity
    FROM product p,bill_items bi,bill b
    WHERE p.pid=bi.productid
    AND bi.billid=b.id
    AND DATE(b.billdate)
    BETWEEN %s AND %s
    GROUP BY p.pid,p.name
    ORDER BY sold_quantity DESC;
    """

    displayReport(sql, (start_date, end_date))


 

 
def SalesReport():

    print("\n========== SALES REPORT ==========\n")

    start_date = input("Enter Start Date (YYYY-MM-DD) : ")

    end_date = input("Enter End Date (YYYY-MM-DD) : ")

    sql = """
    SELECT
    DATE_FORMAT(billdate,'%d-%m-%Y') AS bill_date,
    DAYNAME(billdate) AS day_name,
    COUNT(id) AS total_bills,
    SUM(amount) AS total_sales
    FROM bill
    WHERE DATE(billdate) BETWEEN %s AND %s
    GROUP BY DATE(billdate),DAYNAME(billdate)
    ORDER BY DATE(billdate);
    """

    displayReport(sql, (start_date, end_date))