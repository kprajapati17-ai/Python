class person:
    def walk(self):
        print("I can Walk P")
    def talk(self):
        print("I can Talk P")
    def eat(self):
        print("I can Eat P")

class student(person):
    def read(self):
        print("I can Read P")
    def write(self):
        print("I can Write P")
    def WatIcanDo(self):
        self.read()
        self.write()
        super().walk()
        super().talk()
        super().eat()
     

s1 = student()
s1.walk()
s1.talk()
s1.eat()
s1.read()
s1.write()
print("*"*100)
s1.WatIcanDo()
# *****************************************************************************************************************************************
# OOP 
# --------------------
# 1) Create class Animal which has below method 
#     hunt()
#     reproduce()

# Create class Bird which has below method  and it also extends Animal 
#     fly()
#     nest()
#     cheepering()

class Animal:
    def hunt(self):
        print("Animal can hunt A")
    def reproduce(self):
        print("Animal can reproduce A")


class Bird(Animal):
    def fly(self):
        print("Bird can fly B")
    def nest(self):
        print("Bird can nest B")
    def cheepering(self):
        print("Bird can cheepering B")
    def WatcanDo(self):
        self.fly()
        self.nest()
        self.cheepering()
        super().hunt()
        super().reproduce()

     

s1 = Bird()
s1.hunt()
s1.reproduce()
s1.fly()
s1.nest()
s1.cheepering()
print("*"*100)
s1.WatcanDo()