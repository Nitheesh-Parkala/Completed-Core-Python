import time
from threading import Thread
class Task1(Thread):
    def run(self):
        for i in range(0,100,2):
            print(i)
            time.sleep(2)
class Task2(Thread):
    def run(self):
        for j in range(1,101,2):
            print(j)
            time.sleep(2)
t1=Task1()
t2=Task2()
t1.start()
t2.start()