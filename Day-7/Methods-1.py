# Type1: Method is not accepting the parameter doesn't have any return type.
class Calculator:
    def __init__(self):
        self.x = 10
        self.y = 20
    def disp(self):
        a=100
        b=200
        c=a+b
        print(c) # here it not return any value.
c1= Calculator()
print(c1.x)
print(c1.y)

c1.disp() #here it will not pass any parameter.
