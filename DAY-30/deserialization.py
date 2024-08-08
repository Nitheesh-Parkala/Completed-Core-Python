import pickle

class Employee:
    def __init__(self,name,age,sal,dept):
        self.ename=name
        self.eage=age
        self.esal=sal
        self.edept=dept
    def disp(self):
        print(self.ename)
        print(self.eage)
        print(self.edept)
        print(self.esal)

f=open("employee.txt","rb")
e=pickle.load(f)
e.disp()

print("Object is retrieved from file")
f.close()