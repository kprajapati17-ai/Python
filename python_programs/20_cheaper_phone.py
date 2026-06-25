# 6) write a program to findout which is cheaper approach to buy IPhone 17 pro max.  consider use is going usa should he buy iphone from usa or from india. 

india_price = int(input("Enter the price of iPhone 17 pro max in India in ruppys: "))

usa_price=int(input("Enter the price of iPhone 17 pro max in USA in USD: "))

usa_price_in_rupees = usa_price * 80  # Assuming 1 USD = 80 INR

if india_price < usa_price_in_rupees:
    print("India is cheaper")
else:
    print("USA is cheaper")


