# Type 1: Function with no parameters and no return value
def fun1():
    a=10
    b=20
    c=a*b
    print(c)
fun1()

#Type 2: Function with no parameters but with a return value
def fun2():
    a=10
    b=20
    c=a*b
    return c
r1=fun2()
print(r1)

#Type 3: Function with parameters and no return value
def fun3(a,b):
    c=a*b
    print(c)

x=10
y=20
fun3(x,y)

#Type 4 Function with parameters and a return value
def fun4(a,b):
    c=a*b
    return c

x=10
y=20
r2=fun4(x,y)
print(r2)