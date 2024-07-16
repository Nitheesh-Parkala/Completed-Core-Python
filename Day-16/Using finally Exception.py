# It defines a block of code to run when the try... except...else block is final. 
# The finally block will be executed no matter if the try block raises an error or not.
#  This can be useful to close objects and clean up resources.
def fun1():
    print("Entering fun1")
    try:
        fun2()
    except Exception as e:
        print("Error in fun1")
        raise e
    finally:
       print("Leaving fun1")

def fun2():
    print("Entering fun2")
    try:
        res=10/0
        print(res)
    except Exception as e:
        print("Error in fun2")
        raise e
    finally:
       print("Leaving fun2")

print("Prg Started...")
try:
    fun1()
except Exception as e:
    print("Error in Main") 
print("Prg Ended...")


# try:
#     # Code that might raise an exception
# except SomeException:
#     # Code to handle the exception
# finally:
#     # Code that will always execute
