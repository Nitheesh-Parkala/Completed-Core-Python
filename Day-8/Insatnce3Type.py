#Creating Instance 3 approach of Variable(Diff Btw Instance,Static & Stack)

# Class definition
class Demo():
    # Class variable (static variable)
    x = 10
    
    # Constructor method
    def __init__(self):
        # Instance variables
        self.y = 20
        self.z = 30

    # Instance method
    def add(self):
        # Local variables (stack variables)
        a = 100
        b = 200
        c = a + b
        print(c)
        
        # Instance variable defined within a method
        self.z1 = 40
        print(self.y) 

# Create an instance of the Demo class
d1 = Demo()

# Accessing instance variables
print(d1.y)  # Output: 20
print(d1.z)  # Output: 30

# Accessing class variable
print(Demo.x)  # Output: 10

# Calling instance method
d1.add()  # Output: 300 (from print(c)), 20 (from print(self.y))

# Adding a new instance variable dynamically
d1.y2 = 50
print(d1.y2)  # Output: 50
