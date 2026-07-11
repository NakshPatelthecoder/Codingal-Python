class Dog:
    # Class variable
    animal = "Dog"

    # Constructor
    def __init__(self, breed, age):
        # Instance variables
        self.breed = breed
        self.age = age

    # Method to display details
    def display(self):
        print("Animal:", Dog.animal)
        print("Breed:", self.breed)
        print("Age:", self.age)
        print()


# Create two dog objects
dog1 = Dog("Labrador", 3)
dog2 = Dog("Beagle", 5)

# Display their details
dog1.display()
dog2.display()