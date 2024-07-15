#Type1
def fun1():
    a=10
    b=20
    c=a*b
    print(c)
fun1()

#Type2
def fun2():
    a=10
    b=20
    c=a*b
    return c
r1=fun2()
print(r1)

#Type3
def fun3(a,b):
    c=a*b
    print(c)

x=10
y=20
fun3(x,y)

#Type4
def fun4(a,b):
    c=a*b
    return c

x=10
y=20
r2=fun4(x,y)
print(r2)