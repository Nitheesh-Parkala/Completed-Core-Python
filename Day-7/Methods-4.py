#Methods Having both parameter and return value.

class Calculator:
    def __init__(self):
        self.x = 10
        self.y= 20
    def disp(self,a,b):
        c=a+b
        return c
c1= Calculator()
print(c1.x)
print(c1.y)
n1=100
n2=200
res= c1.disp(n1,n2)
print(res)