#Actual and Formal Parameter
class Demo:
    def swap(self,x,y):
        temp=x
        x= y
        y=temp
        
    
d=Demo()
a=10
b=20
print("Before Swap")
print(a)
print(b)

d.swap(a,b)
print("After Swap")
print(a)
print(b)