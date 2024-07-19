a=10
def fun1():
    print(a)
    b=20
    print(b)

    def fun2():
        print(a)
        b=200
        c=30
        print(b)
        print(c)
    fun2()
    print(b)
print(a)
fun1()