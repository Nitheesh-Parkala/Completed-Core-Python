class Fan:
    def __init__(self):
        self.brand = "Usha"
        self.color = "Black"
        self.cost = 2500
        print(self)
    def rotate(self):
        print("Fan is Rotating")
f1=Fan()
print(f1)
f2=f1
print(f1)
print(f2)

print(id(f1))
print(id(f2))
print(f1 is f2)
