class Person:
    def __init__(self):
        self.__name = ""
    def getter(self):
        return self.__name
    def setter(self,value):
        self.__name=value
        
    getset=property(getter,setter)

p=Person()
p.getset="Rama"
res=p.getset
print(res)