#It will provide the control access to the private member of the class.

class Book:
    def __init__(self,value):
        self.__pages = value
    def setter(self,value):
        if(value>0):
          self.__pages= value
    def getter(self):
       return self.__pages
    
b1=Book(100)
res=b1.getter()
print(res)  # O/P-> 100

b1.setter(200) 
# res = b1.getter() #if this line is not executed then output will get 100 only
print(res) #O/p -> 200

b1.setter(-1)
res=b1.getter()
print(res)  #O/P -> 200