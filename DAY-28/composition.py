class Os:
    def __init__(self):
        self.status=True
        print("Os Is Installing")
    def getOs(self):
        print("Os is still installing...")

class Mobile:
    def __init__(self,name):
        self.mname=name
        self.o=Os()
        print("Mobile is ready")
        print("with os Installed")

m=Mobile("Iphone")

print(m.mname)
print(m.o.status)
m.o.getOs
del m

print(m.o.status)
m.o.getOs