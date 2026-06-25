
class KB():
    def __init__(self,bytes):
        self.bytes =bytes

    def getKB(self):
        kb = self.bytes/1024
        return kb
    
class MB(KB):
    def __init__(self, bytes):
        super().__init__(bytes)
    def getMB(self):
        mb = super().getKB()/1024
        return mb

bt =int(input("Enter Bytes:"))    
m1 = MB(bt) 

mb=m1.getMB()
kb=m1.getKB()
print(f"MB:{mb}  || KB:{kb} ||BYTES:{bt}")       