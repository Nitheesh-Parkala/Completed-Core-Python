class Hero:
    def __init__(self):
        # Initializing the attributes of the Hero class
        self.name = "DBoss"  # Setting the name of the hero
        self.age = 47  # Setting the age of the hero
        self.height = 6.2  # Setting the height of the hero
        self.add = "Rr Nagara"  # Setting the address of the hero

    def act(self):
        # Method to simulate the hero acting
        print("Hero Is Acting")

    def fight(self):
        # Method to simulate the hero fighting
        print("Hero Is Fighting")

# Creating an instance of the Hero class
h1 = Hero()

# Accessing and printing the name of the hero
print(h1.name)  # Output: DBoss

# Accessing and printing the age of the hero
print(h1.age)  # Output: 47

# Accessing and printing the height of the hero
print(h1.height)  # Output: 6.2

# Accessing and printing the address of the hero
print(h1.add)  # Output: Rr Nagara

# Calling the act method for the hero instance
h1.act()  # Output: Hero Is Acting

# Calling the fight method for the hero instance
h1.fight()  # Output: Hero Is Fighting

# Adding new attributes to the hero instance
h1.numOfMovies = 54  # Adding a new attribute numOfMovies
h1.wife = 2  # Adding a new attribute wife

# Modifying an existing attribute
h1.height = 6.5  # Updating the height attribute

# Assigning the same instance to new variables
h2 = h1
h3 = h2

# Accessing and printing the new attributes and updated height
print(h1.numOfMovies)  # Output: 54
print(h2.wife)  # Output: 2
print(h3.height)  # Output: 6.5
