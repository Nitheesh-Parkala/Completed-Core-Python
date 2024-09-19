def fun1():
    print("Entering the fun1")

    try:
        fun2()
    except Exception as e:
        print("Error in fun1")
    print("Leaving fun1")

def fun2():
    print("Entering in fun2")
    try:
        res=10/0
        print(res)
    except Exception as e:
        print("Error in fun2")
    print("leaving fun2")
    
print("Main Started")
fun1()
print("Prg End")
