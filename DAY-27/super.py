class A:
    def __init__(self):
        super().__init__()
        self.a=10
class B(A):
    def __init__(self):
        super().__init__()
        self.b=20
class C(B):
    def __init__(self):
        super().__init__()
        self.c=30

cf=C()
print(cf.c)
print(cf.b)
print(cf.a)
   
