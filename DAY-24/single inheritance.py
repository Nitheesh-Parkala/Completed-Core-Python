# A class inherits from one superclass.
class A:
    def dispA(self):
        print("Inside A")
class B(A):
    def dispB(self):
        print("Inside B")


b=B()
b.dispB()
b.dispA()