def fun1():
    print("Inside fun1")

def fun2(x,y):
    z=x+y
    print("sum is",z)

print(fun1) #Here It Will Print address.
fun1()
a=100
b=200
fun2(a,b)

ptr1=fun1
ptr1()  #Invoking a function through variable.

ptr2=fun2
ptr2(50,20) #Invoking function through Variable.