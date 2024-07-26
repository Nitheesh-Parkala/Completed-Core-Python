class Animal:
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")
    def breath(self):
        print("Animal is breathing")

class Tiger(Animal):
     def eat(self):
         print("Tiger hunt & Eat")
class Deer(Animal):
    def eat(self):
         print("Deer will graze & Eat")
  
class Monkey(Animal):
    def eat(self):
         print("Monkey will steal  & Eat")

t= Tiger()
d= Deer()
m=Monkey()

t.eat()
t.sleep()
t.breath()

d.eat()
d.sleep()
d.breath()


m.eat()
m.sleep()
m.breath()