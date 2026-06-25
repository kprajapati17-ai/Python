# create class Product and store below detail 
#     Name, Price, Stock, weight 
#     add constructor 
#     add display method to display all instance variable 
#     add method UpdatePrice which update only price 
#     add method updateStock which update only stock 

class Product():
    def __init__(self,name,price,stock,weight):
        self.name = name
        self.price = price
        self.stock = stock
        self.weight = weight

    def display(self):
        print("NAME:",self.name)
        print("PRICE:",self.price)
        print("STOCK:",self.stock)
        print("WEIGTH:",self.weight)

    def UpdatePrice(self):
        nprice = int(input("Enter New Price:"))
        self.price = nprice

    def UpdateStock(self):
        nstock = int(input("Enter New Stock:"))
        self.stock = nstock  

name = input("Enter Product Name:")
price =int(input("Enter Product price"))
stock =int(input("Enter Product stock"))
weight =int(input("Enter Product weight"))



p1 = Product(name,price,stock,weight)
p1.display()
p1.UpdatePrice()
p1.UpdateStock()
print("Updating data..")
p1.dispaly()
