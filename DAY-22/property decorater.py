class Person:
    def __init__(self):
        self.__name = ""
    @property
    def data1(self):
        return self.__name
    @data1.setter  
    def data1(self,value):
        self.__name=value
        
p=Person()
p.data1="Rama"
res=p.data1
print(res)
