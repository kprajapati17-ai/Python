import product_function as pf
import bill_function as bf

# -------------------------------
# Function for Safe Menu Choice
# -------------------------------
def getChoice(message, minimum, maximum):

    while True:

        choice = input(message)

        if choice == "":
            print("Choice cannot be empty.")
            continue

        if choice.isdigit() == False:
            print("Please enter numbers only.")
            continue

        choice = int(choice)

        if choice < minimum or choice > maximum:
            print(f"Please enter a choice between {minimum} and {maximum}.")
            continue

        return choice


print("=" * 45)
print("         SHOP MANAGEMENT SYSTEM")
print("=" * 45)

while True:

    print("\n========== MAIN MENU ==========")
    print("1. Product Management")
    print("2. Billing Management")
    print("3. Reports")
    print("0. Exit")

    ch = getChoice("Enter Your Choice : ", 0, 3)

    if ch == 1:

        while True:

            print("\n====== PRODUCT MANAGEMENT ======")
            print("1. Add New Product")
            print("2. Update Product")
            print("3. Delete Product")
            print("4. View All Products")
            print("5. Search Product")
            print("0. Back to Main Menu")

            product_ch = getChoice("Enter Your Choice : ", 0, 5)

            if product_ch == 1:
                pf.AddProduct()

            elif product_ch == 2:
                pf.UpdateProduct()

            elif product_ch == 3:
                pf.DeleteProduct()

            elif product_ch == 4:
                pf.ViewProduct()

            elif product_ch == 5:
                pf.SearchProduct()

            else:
                print("\nReturning To Main Menu...")
                break

    elif ch == 2:

        while True:

            print("\n====== BILLING MANAGEMENT ======")
            print("1. Add Item To Bill")
            print("2. Remove Item From Bill")
            print("3. Search Item")
            print("4. Generate Bill")
            print("5. View All Bills Item")
            print("0. Back To Main Menu")

            bill_ch = getChoice("Enter Your Choice : ", 0, 5)

            if bill_ch == 1:
                bf.AddBill()

            elif bill_ch == 2:
                bf.DeleteItemFromBill()

            elif bill_ch == 3:
                bf.SearchItemInBill()

            elif bill_ch == 4:
                bf.GenerateBill()

            elif bill_ch == 5:
                bf.DisplayBillItem()

            else:
                print("\nReturning To Main Menu...")
                break

    elif ch == 3:

        while True:

            print("\n========== REPORTS ==========")
            print("1. Daily Report")
            print("2. Weekly Report")
            print("3. Monthly Report")
            print("4. Product Report")
            print("5. Sales Report")
            print("0. Back To Main Menu")

            report_ch = getChoice("Enter Your Choice : ", 0, 5)

            if report_ch == 1:
                print("\nGenerating Daily Report...")

            elif report_ch == 2:
                print("\nGenerating Weekly Report...")

            elif report_ch == 3:
                print("\nGenerating Monthly Report...")

            elif report_ch == 4:
                print("\nGenerating Product Report...")

            elif report_ch == 5:
                print("\nGenerating Sales Report...")

            else:
                print("\nReturning To Main Menu...")
                break

    else:
        print("\nThank You For Using Shop Management System.")
        print("Have a Nice Day!")
        print("=" * 45)
        break