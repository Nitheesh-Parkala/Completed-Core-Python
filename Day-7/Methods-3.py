#Method which takes the parameter but does not return the value.

class Calculator:
    def __init__(self):
        # Initializing instance variables x and y with values 10 and 20
        self.x = 10
        self.y = 20
    
    def disp(self, a, b):
        # Variable c is the sum of a and b
        c = a + b
        # Print the result
        print(c)
    
# Creating an instance of the Calculator class
c1 = Calculator()

# Accessing and printing the instance variables x and y
print(c1.x)  # Output: 10
print(c1.y)  # Output: 20

# Defining the variables n1 and n2
n1 = 100
n2 = 200

# Calling the disp method with n1 and n2 as arguments
c1.disp(n1, n2)  # This will print the sum of n1 and n2, which is 300
