# create class Book and store below detail 
#     class should have class variable publisher 
#     Name, author, price, pages 

#     add constructor 
#     add display method to display all instance variable 
#     create multiple object of Book class


class Book:
    publisher = "Gujarati Publications"   # class variable

    def __init__(self, name, author, price, pages):
        self.name = name
        self.author = author
        self.price = price
        self.pages = pages

    def display(self):
        print("Name:", self.name)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Pages:", self.pages)
        print("Publisher:", self.publisher)
        print("----------------------")


# Multiple objects
b1 = Book("Python Basics", "John", 300, 250)
b2 = Book("Data Science", "Alice", 500, 400)
b3 = Book("AI Guide", "David", 700, 350)

# Display
b1.display()
Book.publisher="KP BHAI"
b1.display()

b2.display()
b3.display()