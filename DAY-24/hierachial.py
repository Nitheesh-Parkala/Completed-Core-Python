class A:
    def disA(self):
        print("Inside A")
class B(A):
    def disB(self):
        print("inside B")
class C(A):
    def disC(self):
        print("inside C")

c=C()
c.disC()