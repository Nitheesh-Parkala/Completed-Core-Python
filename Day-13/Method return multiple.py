#Method returning Multiple value
class Demo:
    def arith_op(self,x,y):
        z1=x+y
        z2=x-y
        z3=x*y
        z4=x/y
        return z1,z2,z3,z4
d= Demo()
a=10
b=20

r1,r2,r3,r4 = d.arith_op(a,b)
print(r1)
print(r2)
print(r3)
print(r4)
