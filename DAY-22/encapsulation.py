class Person:
    def __init__(self):
        self.__name=""
    def getter(self):
        return self.__name
    def setter(self,value):
        self.__name = value
p= Person()
p.setter("Rama")
res=p.getter()
print(res)