# PART 1: Create the parent class with shared family traits.
class FamilyMember:
    def __init__(self, eye_colour, height_cm):
        self.eye_colour = eye_colour
        self.height_cm = height_cm

    def show_traits(self):
        print("The eye colour is",self.eye_colour)
        print("The height is",self.height_cm)


# PART 2: Create the child class that inherits from FamilyMember.
class Kid(FamilyMember):


    # PART 3: Give Kid its own details, + the inherited traits from FamilyMember
    def __init__(self,name, age, eye_colour, height_cm):
        self.name = name
        self.age = age
        super().__init__(eye_colour, height_cm)


    # PART 4: Ovveride show_traits to add the Kid's own details too.
    def show_traits(self):
        print(" The name is", self.name)
        print(" The age is", self.age)
        super().show_traits()


    # PART 5: Add a brand new method that only Kid has.
    def favourite_hobby(self, hobby):
        print(self.name, "loves", hobby)


# PART 6: Create a Kid object with real family trait values.
child = Kid("Maya", 10, "brown", 140)


# PART 7: Call the overriden method and the new method.
child.show_traits()
child.favourite_hobby("painting")


# PART 8: Check whether Kid is really a subclass of FamilyMember.
print("Is Kid a subclass of FamilyMember?", issubclass(Kid, FamilyMember))