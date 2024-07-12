#Here we r repeating multiple times without returning

class Demo:
    def add(self,x,y):
        z1=x+y
        return z1
    def sub(self,x,y):
        z2=x-y
        return z2
    def mul(self,x,y):
        z3=x*y
        return z3
d=Demo()
a=10
b=20
r1=d.add(a,b)
r2=d.sub(a,b)
r3=d.mul(a,b)
print(r1)
print(r2)
print(r3)