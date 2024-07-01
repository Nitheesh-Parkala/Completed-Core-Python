class Student:
    def __init__(self):
        self.name ="Nitheesh Prabhu"
        self.age= 23
        self.mob = 9845684599
        self.add = "Parkala"
    def eat(self):
        print("student is eating")
    def study(self):
        print("Student is studying")
s= Student()
print(s.name)
print(s.age)
print(s.mob)
print(s.add)

s.eat()
s.study()
