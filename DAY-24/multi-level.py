class A:
    def dispA(self):
        print("Inside A")
class B(A):
    def dispB(self):
        print("Inside B")
class C(B):
    def dispC(self):
        print("Inside C")

b=C()
b.dispC()
b.dispB()
b.dispA()