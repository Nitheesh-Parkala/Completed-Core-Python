class Cargoplane:
    def takeoff(self):
        print("Plane is take Off")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("plane is landing")
    def carryc(self):
        print("plane carry cargo")

class Passengerplane:
    def takeoff(self):
        print("Plane is take Off")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("plane is landing")
    def carryc(self):
        print("plane  carry passenger")

class Fighterplane:
    def takeoff(self):
        print("Plane is take Off")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("plane is landing")
    def carryc(self):
        print("plane carry weapons")

c=Cargoplane()
p=Passengerplane()
f=Fighterplane()

c.takeoff()
c.fly()
c.land()
c.carryc()

p.takeoff()
p.fly()
p.land()
p.carryc()

f.takeoff()
f.fly()
f.land()
f.carryc()
