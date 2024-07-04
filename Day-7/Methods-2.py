#method is not accepting any parameter but return value.

class Calculator:
    def __init__(self):
        # Initializing instance variables x and y with values 10 and 20
        self.x = 10
        self.y = 20
    
    def disp(self):
        # Local variables a and b are initialized with values 100 and 200
        a = 100
        b = 200
        # Variable c is the sum of a and b
        c = a + b
        return c # The method returns the value of c
    
# Creating an instance of the Calculator class
c1 = Calculator()

# Accessing and printing the instance variables x and y
print(c1.x)  # Output: 10
print(c1.y)  # Output: 20

# Calling the disp method, which does not take any parameters
res = c1.disp()  # The method will return the sum of 100 and 200

# Printing the result of the disp method
print(res)  # Output: 300
