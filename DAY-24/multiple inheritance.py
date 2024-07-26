class A:
    def display(self):
        print("Inside A")
class B:
    def display(self):
        print("Inside B")
class C(A,B):
    def display(self):
        print("Inside C")

c= C()
c.display()
A.display()