class A:
    def display(self):
        print("Inside A")
class B(A):
    def display(self):
        print("Inside B")
class C(B):
    def display(self):
        print("Inside C")
class D(C):
    def dispD(self):
        A.display(self)
        B.display(self)
        C.display(self)
d1=D()
d1.dispD()