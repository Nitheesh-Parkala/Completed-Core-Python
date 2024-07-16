a=10
def fun1():
    a=100
    b=20
    print(a)
    print(b)

def fun2():
    print(a)
    a=1000 #Here we will get error because variable name is same inside the function.
    c=30
    print(a)
    print(c)
print(a)

fun1()
fun2()
print(a)