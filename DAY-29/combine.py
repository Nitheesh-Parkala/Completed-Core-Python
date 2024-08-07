class Heart: 
    def __init__(self,name):
        self.hname=name
        print("heart is Ready")
    
    def getHeart(self):
        print("heart is Beating")

class Person:
    def __init__(self,name):
        self.pname=name
        self.p1=""
        self.p=Heart("abc")
        print("person is ready...")
    def hasPerson(self,pf):
        self.p1=pf
        print("This is a person")

class Car:
    def __init__(self,name):
        self.cname= name
        print("car is ready")
    def getCar(self):
        print("Car is moving")

p2=Person("Rama")
cf=Car("kia")

p2.hasPerson(cf)
print(p2.pname)
print(p2.p.hname)
p2.p.getHeart()
print(p2.p1.cname)
p2.p1.getCar()

del p2
print(cf.cname)
cf.getCar()




