class Fan:
    def __init__(self):
        # Initializing the attributes of the Fan class
        self.brand = "Usha"  # Setting the brand of the fan
        self.color = "White"  # Setting the color of the fan
        self.cost = 2000  # Setting the cost of the fan

    def on(self):
        # Method to turn the fan on
        print("Fan Is On")

    def rotate(self):
        # Method to rotate the fan
        print("Fan is Rotating")

# Creating an instance of the Fan class
f = Fan()

# Accessing and printing the brand of the fan
print(f.brand)  # Output: Usha

# Accessing and printing the color of the fan
print(f.color)  # Output: White

# Accessing and printing the cost of the fan
print(f.cost)  # Output: 2000

