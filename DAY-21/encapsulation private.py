class Book:
    def __init__(self,value):
        self.__pages= value
b1=Book(100)
print(b1.__pages)  #error
b1.pages = 112
print(b1.pages)