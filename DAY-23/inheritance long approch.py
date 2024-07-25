class A:
    def __init__(self):
        self.a1=100
class B:
    def __init__(self):
        A.__init__(self)
        self.b1=200
class C:
    def __init__(self):
        B.__init__(self)
        self.c1=300
cf=C()
print(cf.c1)
print(cf.b1)
print(cf.a1)