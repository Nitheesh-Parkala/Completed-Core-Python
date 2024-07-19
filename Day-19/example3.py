a=10
def fun1():
    global a
    a=100
    b=20
    print(a) #100
    print(b) #20

    def fun2():
        global a
        a=1000
        nonlocal b
        b=200
        c=30
        print(a) #1000
        print(b) #200
        print(c) #30
    print(a)   #100
    print(b)   #20
    fun2()
    print(b)  #200
print(a)  #10
fun1()
print(a)  #1000