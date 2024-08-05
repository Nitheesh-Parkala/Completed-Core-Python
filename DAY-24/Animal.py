#pass is a way to tell Python "do nothing here" while still maintaining the syntactic integrity of your code.
class Animal:
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")
    def breath(self):
        print("Animal is breathing")

class Tiger(Animal):
     pass
class Deer(Animal):
    pass
  
class Monkey(Animal):
    pass

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