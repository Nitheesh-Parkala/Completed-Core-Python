class Charger:
    def __init__(self,name):
        self.cname=name
        print("Charger is ready...")
    
    def getCharger(self):
        print("Charger is Ready to use...")

class Mobile:
    def __init__(self,name):
        self.mname=name
        self.c1= ""
        print("Mobile is ready..")
        print("Mobile & Charger is connected")

    def hasMobile(self,c):
        self.c1=c
        print("Mobile & Charger is connected")

m=Mobile("iphone")
charger=Charger("Iphone Charger")

m.hasMobile(charger)
print(m.mname)
print(m.c1.cname)
m.c1.getCharger()

print("====")

del m
print(charger.cname)
charger.getCharger()

