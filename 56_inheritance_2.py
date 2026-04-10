
# example multilevel inheritance 
class person:
    def walk(self):
        print("I can Walk P")
    def talk(self):
        print("I can Talk P")
    def eat(self):
        print("I can Eat P")

class student(person):
    def read(self):
        print("I can Read S")
    def write(self):
        print("I can Write S")
    def WatIcanDo(self):
        self.read()
        self.write()
        super().walk()
        super().talk()
        super().eat()
     
class devloper(student):
    def code(self):
        print("I can code D")
    def debuge(self):
        print("I can debuge D")
    def WatIcanDo(self):
        self.code()
        self.debuge()
        super().read()
        super().write()
        super().talk()
        super().WatIcanDo()
        super().eat()


s1 = devloper()
s1.code()
s1.debuge()
s1.walk()
s1.talk()
s1.eat()
s1.read()
s1.write()
print("*"*100)
s1.WatIcanDo()
