def fun1():
    a=10
    print(a)  #First this will print

    def fun2():
        b=20
        print(a) #Third this will print
        print(b) #Fourth this will print
    print(a)  #Second this will print
    print(b)  #Error
    fun2()
    print(b)  #Error
fun1()