a=10

def fun1():
    global a  #This comment is used to modify the global value.
    a=100
    b=20
    print(a)
    print(b)

def fun2():
    global a
    a=1000
    c=30
    print(a)
    print(c)

print(a)
fun1()
fun2()
print(a)
    