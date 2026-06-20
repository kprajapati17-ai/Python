

# 2) Create class Foot which has constructor to initialize inches 
#     and it getFoot() method which return foot 

# Create class meter which extends Foot class 
#     and it getMeter() method which return meter 

class Foot():
    def __init__(self,inches):
        self.inches =inches

    def getFOOT(self):
        f = self.inches/12
        return f
    
class Meter(Foot):
    def __init__(self, inches):
        super().__init__(inches)
    def getMeter(self):
        m = super().getFOOT() * 0.3048
        return m

i =int(input("Enter Inches:"))    
m1 = Meter(i) 

f=m1.getFOOT()
m=m1.getMeter()
print(f"FOOT:{f}  || METER:{m} ||INCHES:{i}")       