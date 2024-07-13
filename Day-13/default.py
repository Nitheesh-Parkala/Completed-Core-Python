class Demo:
    def add(self,x=11,y=22,z=33): #Passing Default value
        print(x)
        print(y)
        print(z)
d=Demo()
a=10
b=20
c=30

d.add(a,b,c) #O/P-> 10,20,30
d.add(a,b) #It will throw Error so we should pass default value -> O/P-> 10,20,30
d.add(a) # O/P-> 10,22,33
d.add()  # O/P-> 11,22,33
d.add(c) # O/p-> 30,22,33
d.add(b,c) # O/P -> 20,30,33
d.add(z=c)
d.add(y=b,z=c)
d.add(x=a,y=b,z=c)