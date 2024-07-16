def fun1():
    print("Entering fun1")

    try:
        fun2()
    except Exception as e:
        print("leaving fun1")

def fun2():
    print("Entering fun2")
    res=10/0
    print(res)
    print("Leaving fun2")

print("Main Started")
fun1()
print("Prg Ended")