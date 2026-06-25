print("=" * 45)
print("         SHOP MANAGEMENT SYSTEM")
print("=" * 45)

while True:
    print("\n========== MAIN MENU ==========")
    print("1. Product Management")
    print("2. Billing Management")
    print("3. Reports")
    print("0. Exit")

    ch = int(input("Enter Your Choice : "))

    if ch < 0 or ch > 3:
        print("\nInvalid Choice. Please Try Again.")

    elif ch == 1:
        while True:
            print("\n====== PRODUCT MANAGEMENT ======")
            print("1. Add New Product")
            print("2. Update Product")
            print("3. Delete Product")
            print("4. View All Products")
            print("5. Search Product")
            print("0. Back to Main Menu")

            product_ch = int(input("Enter Your Choice : "))

            if product_ch < 0 or product_ch > 5:
                print("\nInvalid Choice. Please Try Again.")

            elif product_ch == 1:
                print("\nOpening Add Product Module...")

            elif product_ch == 2:
                print("\nOpening Update Product Module...")

            elif product_ch == 3:
                print("\nOpening Delete Product Module...")

            elif product_ch == 4:
                print("\nOpening Product List...")

            elif product_ch == 5:
                print("\nOpening Product Search...")

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
            print("5. View All Bills")
            print("0. Back To Main Menu")

            bill_ch = int(input("Enter Your Choice : "))

            if bill_ch < 0 or bill_ch > 5:
                print("\nInvalid Choice. Please Try Again.")

            elif bill_ch == 1:
                print("\nOpening Add Item Module...")

            elif bill_ch == 2:
                print("\nOpening Remove Item Module...")

            elif bill_ch == 3:
                print("\nOpening Search Item Module...")

            elif bill_ch == 4:
                print("\nGenerating Bill...")

            elif bill_ch == 5:
                print("\nOpening Bill History...")

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

            report_ch = int(input("Enter Your Choice : "))

            if report_ch < 0 or report_ch > 5:
                print("\nInvalid Choice. Please Try Again.")

            elif report_ch == 1:
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