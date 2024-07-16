#Higher Order Function means- If any function which expect the parameter to the other function is called HOF.
def fun1():  #First Class Function.
    print("Invoked fun1")

def fun2(a,b): #First Class Function.
    res=a+b
    print("sum is",res)

def display(ptr1,ptr2):  #Higher Order Function
    print(ptr1)
    print(ptr2)
    ptr1()
    ptr2(21,26)
   

fun1()
x=10
y=20
fun2(x,y)

ptr3=fun1
ptr4=fun2

ptr3()
ptr4(100,200)

display(ptr3,ptr4)
 
