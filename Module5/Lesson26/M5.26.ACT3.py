class Parrot:

    species = "Bird"

    def __init__(self, name, age):

            self.name = name
            self.age = age

Blu = Parrot("Blu", 10)
Woo = Parrot("Woo", 15)

print("Blu's species is ", Blu.species)
print("Woo's species is ", Woo.species)

print("Bird - Blu - Name & Age",Blu.name, Blu.age)
print("Bird - Woo - Name & Age",Woo.name, Woo.age)