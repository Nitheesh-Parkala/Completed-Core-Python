import time
class Demo:
    def printName(self):
        names=["rama","sita","ravana"]

        for data in names:
            print(data)
            time.sleep(3)
    def printNum(self):
        for i in range(10):
            print(i)
            time.sleep(2)
    def add(self):
        a=10
        b=20
        res=a+b
        print(res)
d1=Demo()
d1.printName()
d1.printNum()
d1.add()
