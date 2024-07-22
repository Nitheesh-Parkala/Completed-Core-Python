def fun1():
    print("Inside the fun1") #8 It will print
def fun2(x,y):
    res=x*y
    print(res)  #9 It will print
def fun3(ptr1,ptr2):
    print(ptr1) #6 It will print
    print(ptr2) #7 It will print
    ptr1()
    ptr2(21,26)

print(fun1) #1 It will print
print(fun2) #2 It will print
 
ptr3=fun1
ptr4=fun2
print(ptr3) #3 It will print
print(ptr4) #4 It will print
print("hi") #5 It will print
fun3(ptr3,ptr4)
    