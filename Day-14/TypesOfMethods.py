class Demo:
    x=10 #Static Method
 
    def __init__(self):
        self.y=20
        self.z=30
    def instancedisp(self):  #Instance Method
        print(self.y)
        print(self.z)

    @staticmethod
    def staticdisp():
     print(Demo.x)

    @classmethod
    def classdisp(Demo):
       print("python")

Demo.staticdisp()  #We can create static method without creating the object.
Demo.classdisp()
d=Demo()
d.instancedisp()