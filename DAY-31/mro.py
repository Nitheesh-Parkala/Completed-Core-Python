class A:
    def dispA(self):
        print("Inside A")

print(A.mro())

class B:
    def dispB(self):
     print("Inside B")

print(B.mro())

class C(A,B):
   def dispC(self):
      print("Inside c")

print(C.mro())