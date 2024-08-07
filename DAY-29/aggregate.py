class Charger:
    def __init__(self,name):
        self.cname=name
        print("Charger is ready...")
    
    def getCharger(self):
        print("Charger is Ready to use...")

class Mobile:
    def __init__(self,name):
        self.mname=name
        self.c1= Charger("xyz")
        print("Mobile & Charger is connected")
    def getMobile(self):
        self.c1.getCharger()
        print("Mobile is ready..")

m=Mobile("iphone")
print(m.mname)
print(m.c1.cname)
m.getMobile()

del m

# print(.mname)
Charger.getCharger()
