class Plane:
    def takeoff(self):
         print("Plane is take Off")
    def fly(self):
         print("Plane is flying")
    def land(self):
         print("Plane is landing")

class Cargo(Plane):
     def carryc(self):
          print("plane carry cargo")

class Passenger(Plane):
     def carryc(self):
          print("Plane carry passengers")

class  Fighter(Plane):
     def carryc(self):
          print("Flight carry weapons")

# Create instances of Cargo and Passenger
f=Cargo()
p=Passenger()

# Call methods on Cargo instance
f.takeoff()
f.fly()
f.land()
f.carryc()

# Call methods on Cargo instance
f.takeoff()
f.fly()
f.land()
f.carryc()